"""
AI Visibility Monitor API Service
FastAPI-based web service for DataForSEO AI visibility analysis
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import os
import json
import asyncio
from datetime import datetime
import uuid
from ai_visibility_monitor import AIVisibilityMonitor, UserInput

# Initialize FastAPI app
app = FastAPI(
    title="AI Visibility Monitor API",
    description="DataForSEO-powered AI search visibility tracking service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for API requests/responses
class AnalysisRequest(BaseModel):
    brand_name: str = Field(..., description="Brand name to analyze")
    brand_domain: str = Field(..., description="Brand domain (e.g., nike.com)")
    competitors: List[str] = Field(default=[], description="List of competitor domains")
    serp_queries: List[str] = Field(..., description="Keywords to analyze")
    industry: str = Field(default="General", description="Industry category")
    location: str = Field(default="United States", description="Geographic location")
    device: str = Field(default="desktop", description="Device type (desktop/mobile/tablet)")
    language: str = Field(default="English", description="Language for analysis")

class AnalysisStatus(BaseModel):
    analysis_id: str
    status: str  # "pending", "running", "completed", "failed"
    progress: Optional[int] = None
    message: Optional[str] = None
    started_at: datetime
    completed_at: Optional[datetime] = None

class AnalysisResult(BaseModel):
    analysis_id: str
    status: str
    request: AnalysisRequest
    results: Optional[List[Dict[str, Any]]] = None
    summary: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    started_at: datetime
    completed_at: Optional[datetime] = None

# In-memory storage for analysis jobs (use Redis/database in production)
analysis_jobs: Dict[str, AnalysisResult] = {}

# Health check endpoint
@app.get("/")
async def root():
    return {
        "service": "AI Visibility Monitor API",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for Render"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "ai-visibility-monitor"
    }

@app.post("/api/v1/analyze", response_model=AnalysisStatus)
async def start_analysis(request: AnalysisRequest, background_tasks: BackgroundTasks):
    """Start a new AI visibility analysis"""
    
    # Validate credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        raise HTTPException(
            status_code=500, 
            detail="DataForSEO credentials not configured"
        )
    
    # Generate unique analysis ID
    analysis_id = str(uuid.uuid4())
    
    # Create analysis job
    analysis_job = AnalysisResult(
        analysis_id=analysis_id,
        status="pending",
        request=request,
        started_at=datetime.now()
    )
    
    analysis_jobs[analysis_id] = analysis_job
    
    # Start background analysis
    background_tasks.add_task(run_analysis, analysis_id, request, login, password)
    
    return AnalysisStatus(
        analysis_id=analysis_id,
        status="pending",
        message="Analysis started",
        started_at=analysis_job.started_at
    )

@app.get("/api/v1/analysis/{analysis_id}", response_model=AnalysisResult)
async def get_analysis(analysis_id: str):
    """Get analysis results by ID"""
    
    if analysis_id not in analysis_jobs:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    return analysis_jobs[analysis_id]

@app.get("/api/v1/analysis/{analysis_id}/status", response_model=AnalysisStatus)
async def get_analysis_status(analysis_id: str):
    """Get analysis status by ID"""
    
    if analysis_id not in analysis_jobs:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    job = analysis_jobs[analysis_id]
    
    # Calculate progress for running jobs
    progress = None
    if job.status == "running" and job.results:
        progress = len(job.results)
    
    return AnalysisStatus(
        analysis_id=analysis_id,
        status=job.status,
        progress=progress,
        message=f"Analysis {job.status}",
        started_at=job.started_at,
        completed_at=job.completed_at
    )

@app.get("/api/v1/analyses")
async def list_analyses():
    """List all analyses"""
    return {
        "analyses": [
            {
                "analysis_id": job.analysis_id,
                "status": job.status,
                "brand_name": job.request.brand_name,
                "started_at": job.started_at,
                "completed_at": job.completed_at
            }
            for job in analysis_jobs.values()
        ]
    }

async def run_analysis(analysis_id: str, request: AnalysisRequest, login: str, password: str):
    """Background task to run the analysis"""
    
    try:
        # Update status
        analysis_jobs[analysis_id].status = "running"
        
        # Create user input
        user_input = UserInput(
            brand_name=request.brand_name,
            brand_domain=request.brand_domain,
            competitors=request.competitors,
            serp_queries=request.serp_queries,
            industry=request.industry,
            location=request.location,
            device=request.device,
            language=request.language
        )
        
        # Run analysis
        monitor = AIVisibilityMonitor(login, password)
        results = monitor.run_analysis(user_input)
        
        # Convert results to JSON-serializable format
        results_data = [
            {
                "query": result.query,
                "location": result.location,
                "device": result.device,
                "timestamp": result.timestamp,
                "google_ai_overview_present": result.google_ai_overview_present,
                "google_brand_cited": result.google_brand_cited,
                "google_ai_citations": result.google_ai_citations,
                "google_competitor_citations": result.google_competitor_citations,
                "bing_ai_features": result.bing_ai_features,
                "bing_brand_visibility": result.bing_brand_visibility,
                "featured_snippet_present": result.featured_snippet_present,
                "knowledge_graph_present": result.knowledge_graph_present,
                "people_also_ask_present": result.people_also_ask_present
            }
            for result in results
        ]
        
        # Generate summary
        total_queries = len(results)
        ai_overview_count = sum(1 for r in results if r.google_ai_overview_present)
        brand_citation_count = sum(1 for r in results if r.google_brand_cited)
        
        summary = {
            "total_queries": total_queries,
            "ai_overview_presence": {
                "count": ai_overview_count,
                "percentage": round((ai_overview_count / total_queries) * 100, 1) if total_queries > 0 else 0
            },
            "brand_citations": {
                "count": brand_citation_count,
                "percentage": round((brand_citation_count / ai_overview_count) * 100, 1) if ai_overview_count > 0 else 0
            }
        }
        
        # Update job with results
        analysis_jobs[analysis_id].status = "completed"
        analysis_jobs[analysis_id].results = results_data
        analysis_jobs[analysis_id].summary = summary
        analysis_jobs[analysis_id].completed_at = datetime.now()
        
        # Save results to file
        filename = f"results/api_analysis_{analysis_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        os.makedirs('results', exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump({
                "analysis_id": analysis_id,
                "request": request.dict(),
                "results": results_data,
                "summary": summary
            }, f, indent=2)
        
    except Exception as e:
        # Update job with error
        analysis_jobs[analysis_id].status = "failed"
        analysis_jobs[analysis_id].error = str(e)
        analysis_jobs[analysis_id].completed_at = datetime.now()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
