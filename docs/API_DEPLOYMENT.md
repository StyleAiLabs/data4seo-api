# AI Visibility Monitor API

## 🚀 **Render Deployment Guide**

### **Deployment Steps**

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add API service for Render deployment"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Click "New Web Service"
   - Connect your GitHub repository
   - Choose "ai-visibility-monitor" service
   - Render will auto-detect `render.yaml`

3. **Set Environment Variables**:
   ```
   DATAFORSEO_LOGIN=your_login
   DATAFORSEO_PASSWORD=your_password
   ```

4. **Deploy**: Click "Create Web Service"

---

## 📚 **API Documentation**

### **📋 Quick Reference - All Available Endpoints**

| Method | Endpoint | API Version | Response Time | Purpose |
|--------|----------|-------------|---------------|---------|
| `GET` | `/` | v1/v2 | Instant | Service information |
| `GET` | `/health` | v1/v2 | Instant | Health check |
| `POST` | `/api/v1/analyze` | v1 | 2-5 minutes | Start comprehensive analysis |
| `GET` | `/api/v1/analysis/{id}/status` | v1 | Instant | Check analysis progress |
| `GET` | `/api/v1/analysis/{id}` | v1 | Instant | Get complete results |
| `GET` | `/api/v1/analyses` | v1 | Instant | List all analyses |
| `POST` | `/api/v2/onboarding-analysis` | v2 | 15-30 seconds | **⚡ Fast onboarding** |
| `POST` | `/api/v2/fast-analysis` | v2 | 30-45 seconds | **🚀 Quick detailed analysis** |
| `POST` | `/api/v2/batch-onboarding` | v2 | 1-2 minutes | **📊 Batch processing** |
| `GET` | `/api/v2/performance-metrics` | v2 | Instant | Performance stats |
| `GET` | `/api/v2/onboarding-demo` | v2 | Instant | **Demo (no credentials)** |

### **Base URL**
```
https://data4seo-api.onrender.com
```

**🎯 Your deployed service now includes both v1 and v2 endpoints!**

- **Standard API (v1)**: `https://data4seo-api.onrender.com/api/v1/`
- **Fast API (v2)**: `https://data4seo-api.onrender.com/api/v2/` ⚡
- **API Information**: `https://data4seo-api.onrender.com/api/info`
- **Interactive Docs**: `https://data4seo-api.onrender.com/docs`

### **Authentication**
No API key required. DataForSEO credentials are configured server-side.

---

## 🔗 **Complete API Endpoints Reference**

### **📊 Standard API Service (v1) - Comprehensive Analysis**

#### **1. Service Information**
```http
GET /
```
**Response:**
```json
{
  "service": "AI Visibility Monitor API",
  "version": "1.0.0", 
  "status": "running",
  "description": "Comprehensive AI visibility analysis",
  "timestamp": "2025-08-09T14:30:25"
}
```

#### **2. Health Check**
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-08-09T14:30:25",
  "service": "ai-visibility-monitor"
}
```

#### **3. Start Comprehensive Analysis**
```http
POST /api/v1/analyze
Content-Type: application/json
```

**Request Body:**
```json
{
  "brand_name": "Nike",
  "brand_domain": "nike.com",
  "competitors": ["adidas.com", "puma.com", "underarmour.com"],
  "serp_queries": ["running shoes", "athletic wear", "sneakers", "sports gear", "fitness clothing"],
  "industry": "Sports & Fitness",
  "location": "United States",
  "device": "desktop",
  "language": "English"
}
```

**Response:**
```json
{
  "analysis_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "pending",
  "message": "Analysis started",
  "started_at": "2025-08-09T14:30:25"
}
```

#### **4. Get Analysis Status**
```http
GET /api/v1/analysis/{analysis_id}/status
```

**Response:**
```json
{
  "analysis_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running",
  "progress": 3,
  "total_queries": 5,
  "message": "Processing query 3 of 5: sneakers",
  "started_at": "2025-08-09T14:30:25",
  "estimated_completion": "2025-08-09T14:33:25"
}
```

**Status Values:**
- `pending` - Analysis queued
- `running` - Analysis in progress  
- `completed` - Analysis finished successfully
- `failed` - Analysis encountered an error

#### **5. Get Comprehensive Analysis Results**
```http
GET /api/v1/analysis/{analysis_id}
```

**Response:** *(Full detailed analysis with 20+ data points per keyword)*
```json
{
  "analysis_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "completed",
  "request": {
    "brand_name": "Nike",
    "brand_domain": "nike.com",
    "competitors": ["adidas.com", "puma.com"],
    "serp_queries": ["running shoes"],
    "industry": "Sports & Fitness",
    "location": "United States"
  },
  "results": [
    {
      "query": "running shoes",
      "location": "United States",
      "device": "desktop",
      "timestamp": "2025-08-09T14:30:25",
      "google_ai_overview_present": true,
      "google_brand_cited": true,
      "google_ai_citations": ["nike.com", "adidas.com"],
      "google_competitor_citations": {"adidas.com": 1},
      "bing_ai_features": ["answer_box"],
      "bing_brand_visibility": true,
      "featured_snippet_present": true,
      "knowledge_graph_present": false,
      "people_also_ask_present": true,
      "people_also_ask_queries": [
        "What are the best running shoes for beginners?",
        "How often should you replace running shoes?"
      ],
      "bing_people_also_ask_present": true,
      "bing_people_also_ask_queries": [
        "running shoes for flat feet",
        "best running shoes 2025"
      ],
      "ai_visibility_score": 85.0,
      "competitor_ai_scores": {"adidas.com": 70.0, "puma.com": 45.0},
      "ai_dominance_rank": 1
    }
  ],
  "summary": {
    "total_queries": 1,
    "ai_overview_presence": {"count": 1, "percentage": 100.0},
    "brand_citations": {"count": 1, "percentage": 100.0},
    "ai_visibility_scoring": {"average_score": 85.0, "max_score": 100.0},
    "people_also_ask_insights": {
      "google_paa": {"queries_with_paa": 1, "total_questions": 3, "percentage": 100.0},
      "bing_paa": {"queries_with_paa": 1, "total_questions": 3, "percentage": 100.0}
    },
    "competitor_analysis": {"competitor_citations": {"adidas.com": 1}}
  },
  "started_at": "2025-08-09T14:30:25",
  "completed_at": "2025-08-09T14:35:15"
}
```

#### **6. List All Analyses**
```http
GET /api/v1/analyses
```

**Response:**
```json
{
  "analyses": [
    {
      "analysis_id": "123e4567-e89b-12d3-a456-426614174000",
      "status": "completed",
      "brand_name": "Nike",
      "total_queries": 5,
      "started_at": "2025-08-09T14:30:25",
      "completed_at": "2025-08-09T14:35:15",
      "processing_time_minutes": 5.0
    }
  ]
}
```

---

### **⚡ Fast AI Service (v2) - SaaS Optimized**

#### **7. Fast Service Information**
```http
GET /
```
**Response:**
```json
{
  "service": "Fast AI Visibility API",
  "version": "2.0.0",
  "status": "running",
  "optimized_for": "SaaS user onboarding",
  "speed_improvement": "8-10x faster than standard analysis",
  "timestamp": "2025-08-09T14:30:25"
}
```

#### **8. Fast Service Health Check**
```http
GET /health
```
**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-08-09T14:30:25",
  "service": "fast-ai-visibility-api",
  "response_time_target": "< 30 seconds"
}
```

#### **9. Fast Onboarding Analysis (15-30 seconds)**
```http
POST /api/v2/onboarding-analysis
Content-Type: application/json
```

**Optimized for SaaS user onboarding with ultra-fast response times.**

**Request Body:**
```json
{
  "brand_name": "Nike",
  "website": "nike.com",
  "primary_keywords": ["running shoes", "athletic wear"],
  "main_competitors": ["adidas.com"]
}
```

**Response (15-30 seconds):**
```json
{
  "ai_readiness_score": 75.0,
  "visibility_status": "good",
  "key_findings": [
    "AI Overview appears in 67% of your target keywords",
    "Your brand is cited in 50% of AI Overviews",
    "Analysis includes 1 competitors"
  ],
  "immediate_actions": [
    "Optimize content for AI Overview eligibility",
    "Focus on factual, authoritative content creation"
  ],
  "competitive_position": "Analyzed against 1 competitors",
  "processing_time_ms": 18500
}
```

#### **10. Fast Detailed Analysis (30-45 seconds)**
```http
POST /api/v2/fast-analysis
Content-Type: application/json
```

**Request Body:**
```json
{
  "brand_name": "Nike",
  "brand_domain": "nike.com", 
  "competitors": ["adidas.com", "puma.com"],
  "keywords": ["running shoes", "athletic wear", "sneakers"],
  "location": "United States"
}
```

**Response (30-45 seconds):**
```json
{
  "success": true,
  "analysis_id": "fast-abc123",
  "brand_name": "Nike",
  "processing_time_ms": 32000,
  "ai_visibility_score": 78.5,
  "ai_overview_presence": {
    "count": 2,
    "percentage": 66.7
  },
  "brand_citations": {
    "count": 1,
    "percentage": 50.0
  },
  "recommendations": [
    "Strong AI visibility for running shoes",
    "Optimize athletic wear content for AI citations",
    "Monitor competitor activities in sneakers category"
  ],
  "detailed_results": [
    {
      "query": "running shoes",
      "ai_visibility_score": 85.0,
      "google_ai_overview_present": true,
      "google_brand_cited": true,
      "bing_ai_present": true,
      "bing_brand_visible": false,
      "processing_time_ms": 12000
    }
  ],
  "next_steps": {
    "upgrade_to_full": "For comprehensive analysis with 20+ keywords",
    "monitoring_setup": "Set up ongoing monitoring for these keywords"
  },
  "timestamp": "2025-08-09T14:30:25"
}
```

#### **11. Batch Onboarding Analysis**
```http
POST /api/v2/batch-onboarding
Content-Type: application/json
```

**For processing multiple brands simultaneously (max 3):**

**Request Body:**
```json
[
  {
    "brand_name": "Nike",
    "website": "nike.com",
    "primary_keywords": ["running shoes"]
  },
  {
    "brand_name": "Adidas", 
    "website": "adidas.com",
    "primary_keywords": ["athletic wear"]
  }
]
```

**Response (1-2 minutes):**
```json
{
  "batch_results": [
    {
      "brand_name": "Nike",
      "ai_readiness_score": 82.5,
      "processing_time_ms": 18500,
      "status": "completed"
    },
    {
      "brand_name": "Adidas",
      "ai_readiness_score": 71.2,
      "processing_time_ms": 19200,
      "status": "completed"
    }
  ],
  "total_processing_time_ms": 45000,
  "brands_analyzed": 2,
  "average_time_per_brand": 22500
}
```

#### **12. Performance Metrics**
```http
GET /api/v2/performance-metrics
```

**Response:**
```json
{
  "target_response_time": "< 30 seconds",
  "optimization_features": [
    "Parallel SERP fetching",
    "Limited keyword analysis (max 5)",
    "Streamlined result processing",
    "Cached location/language mappings",
    "Connection pooling"
  ],
  "speed_improvements": {
    "serp_fetching": "6x faster with parallel requests",
    "analysis_processing": "4x faster with streamlined logic",
    "overall_improvement": "8-10x faster than standard analysis"
  },
  "scalability": {
    "concurrent_requests": "Optimized for high concurrency",
    "rate_limiting": "Built-in request throttling",
    "resource_usage": "Minimal memory footprint"
  }
}
```

#### **13. Onboarding Demo (No Credentials Required)**
```http
GET /api/v2/onboarding-demo
```

**Response:**
```json
{
  "demo_brand": "Nike",
  "demo_keywords": ["running shoes", "athletic wear", "sportswear"],
  "expected_response_time": "15-25 seconds",
  "demo_results": {
    "ai_readiness_score": 82.5,
    "visibility_status": "excellent",
    "key_findings": [
      "AI Overview appears in 67% of your target keywords",
      "Your brand is cited in 100% of AI Overviews",
      "Strong competitive position in AI search"
    ],
    "processing_time_ms": 18500
  },
  "integration_notes": {
    "use_case": "Perfect for user onboarding flows",
    "user_experience": "Real-time analysis during signup",
    "follow_up": "Offer detailed analysis as premium feature"
  }
}
```

---

## 🧪 **Testing & Usage Examples**

### **Standard API (v1) Testing**

**Start Comprehensive Analysis:**
```bash
curl -X POST "https://your-service.onrender.com/api/v1/analyze" \
     -H "Content-Type: application/json" \
     -d '{
       "brand_name": "Nike",
       "brand_domain": "nike.com",
       "competitors": ["adidas.com", "puma.com"],
       "serp_queries": ["running shoes", "athletic wear", "sneakers"],
       "industry": "Sports",
       "location": "United States",
       "device": "desktop",
       "language": "English"
     }'
```

**Check Analysis Status:**
```bash
curl "https://your-service.onrender.com/api/v1/analysis/ANALYSIS_ID/status"
```

**Get Comprehensive Results:**
```bash
curl "https://your-service.onrender.com/api/v1/analysis/ANALYSIS_ID"
```

### **Fast API (v2) Testing**

**Quick Onboarding Analysis:**
```bash
curl -X POST "https://data4seo-api.onrender.com/api/v2/onboarding-analysis" \
     -H "Content-Type: application/json" \
     -d '{
       "brand_name": "Nike",
       "website": "nike.com",
       "primary_keywords": ["running shoes", "athletic wear"],
       "main_competitors": ["adidas.com"]
     }'
```

**Fast Detailed Analysis:**
```bash
curl -X POST "https://data4seo-api.onrender.com/api/v2/fast-analysis" \
     -H "Content-Type: application/json" \
     -d '{
       "brand_name": "Nike",
       "brand_domain": "nike.com",
       "competitors": ["adidas.com"],
       "keywords": ["running shoes"],
       "location": "United States"
     }'
```

**Demo Endpoint (No Credentials Required):**
```bash
curl "https://data4seo-api.onrender.com/api/v2/onboarding-demo"
```

### **Local Development Testing**

**Start Standard API:**
```bash
uvicorn api_service:app --host 0.0.0.0 --port 8000
```

**Start Fast API:**
```bash
uvicorn fast_api_service:app --host 0.0.0.0 --port 8001
```

**Test Health Endpoints:**
```bash
# Standard API
curl http://localhost:8000/health

# Fast API  
curl http://localhost:8001/health
```

### **Python Client Example**

```python
import requests
import time

# Start analysis
response = requests.post("https://your-service.onrender.com/api/v1/analyze", json={
    "brand_name": "Nike",
    "brand_domain": "nike.com",
    "competitors": ["adidas.com"],
    "serp_queries": ["running shoes"],
    "industry": "Sports",
    "location": "United States",
    "device": "desktop",
    "language": "English"
})

analysis_id = response.json()["analysis_id"]

# Poll for completion
while True:
    status = requests.get(f"https://your-service.onrender.com/api/v1/analysis/{analysis_id}/status")
    status_data = status.json()
    
    if status_data["status"] in ["completed", "failed"]:
        break
    
    print(f"Status: {status_data['status']}")
    time.sleep(10)

# Get results
results = requests.get(f"https://your-service.onrender.com/api/v1/analysis/{analysis_id}")
print(results.json())
```

### **JavaScript/Node.js Example**

```javascript
const axios = require('axios');

async function analyzeVisibility() {
  // Start analysis
  const response = await axios.post('https://your-service.onrender.com/api/v1/analyze', {
    brand_name: 'Nike',
    brand_domain: 'nike.com',
    competitors: ['adidas.com'],
    serp_queries: ['running shoes'],
    industry: 'Sports',
    location: 'United States',
    device: 'desktop',
    language: 'English'
  });

  const analysisId = response.data.analysis_id;

  // Poll for completion
  while (true) {
    const status = await axios.get(`https://your-service.onrender.com/api/v1/analysis/${analysisId}/status`);
    
    if (['completed', 'failed'].includes(status.data.status)) {
      break;
    }
    
    console.log(`Status: ${status.data.status}`);
    await new Promise(resolve => setTimeout(resolve, 10000));
  }

  // Get results
  const results = await axios.get(`https://your-service.onrender.com/api/v1/analysis/${analysisId}`);
  console.log(results.data);
}

analyzeVisibility();
```

---

## 📊 **Interactive API Documentation**

Once deployed, visit these URLs for interactive documentation:

### **Combined API Service Documentation**
- **Swagger UI**: `https://data4seo-api.onrender.com/docs`
- **ReDoc**: `https://data4seo-api.onrender.com/redoc`
- **API Info**: `https://data4seo-api.onrender.com/api/info`

### **Local Development Documentation**
- **Combined API**: `http://localhost:8000/docs`

**Features:**
- ✅ Interactive endpoint testing
- ✅ Request/response examples  
- ✅ Parameter validation
- ✅ Response schema documentation
- ✅ Try-it-now functionality
- ✅ Both v1 and v2 endpoints in one service

---

## 📊 **API Performance Comparison**

| API Version | Endpoint | Response Time | Keywords | Use Case | Concurrent Support |
|-------------|----------|---------------|----------|----------|-------------------|
| **v1** | `/api/v1/analyze` | 2-5 minutes | 20+ keywords | Comprehensive analysis | Background tasks |
| **v2** | `/api/v2/fast-analysis` | 30-45 seconds | 5 keywords | Quick detailed insights | High concurrency |
| **v2** | `/api/v2/onboarding-analysis` | 15-30 seconds | 2-3 keywords | User onboarding | Ultra-fast |
| **v2** | `/api/v2/batch-onboarding` | 1-2 minutes | Multiple brands | Bulk processing | Batch optimized |

### **🎯 When to Use Which API:**

**Standard API (v1)** - Use for:
- 📊 Comprehensive competitor analysis (20+ keywords)
- 📈 Detailed monthly/quarterly reports
- 🔍 In-depth PAA and SERP feature analysis
- 📋 Complete AI visibility audits

**Fast API (v2)** - Use for:
- ⚡ SaaS user onboarding flows
- 🚀 Real-time analysis during demos
- � Freemium product offerings
- 🎯 Quick brand assessments

---

## ⚡ **Performance Notes**

- **Standard Analysis Time**: 2-5 minutes per keyword (depends on API response time)
- **Fast Analysis Time**: 15-45 seconds total (parallel processing)
- **Concurrent Requests**: Supported via background tasks
- **Rate Limiting**: Built-in 1-second delays between DataForSEO calls
- **Results Storage**: JSON files saved to `/results` directory

---

## 🛠 **Production Considerations**

### **For Production Deployment:**

1. **Use Database**: Replace in-memory storage with PostgreSQL/Redis
2. **Add Authentication**: Implement API key authentication
3. **Add Rate Limiting**: Implement client rate limiting
4. **Add Monitoring**: Set up logging and health monitoring
5. **Optimize Storage**: Use cloud storage for results files
6. **Add Caching**: Cache results for duplicate queries

### **Render Scaling:**

- **Starter Plan**: $7/month, suitable for testing
- **Standard Plan**: $25/month, better for production
- **Pro Plan**: $85/month, high-performance applications

---

## 🔒 **Security**

- DataForSEO credentials stored as environment variables
- No API keys exposed in responses
- CORS configured (adjust origins for production)
- Results include no sensitive data

---

## 📞 **Support**

For API issues:
- Check `/health` endpoint
- Review logs in Render dashboard
- Verify DataForSEO credentials in environment variables
