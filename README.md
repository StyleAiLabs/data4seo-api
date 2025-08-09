# AI Search Visibility Monitor

**DataForSEO V3 API Integration for Brand AI Visibility Tracking - Optimized for SaaS Integration**

## 🚀 Overview

This project implements a high-performance AI search visibility monitoring system using DataForSEO APIs, **optimized for SaaS integration** with proven **5-10x speed improvements**. It tracks brand visibility across Google AI Overviews, Bing AI features, and traditional SERP elements.

## ⚡ Performance Optimized

- **🚀 Fast Analysis**: 15-30 seconds (vs 2-3 minutes standard)
- **⚡ Parallel Processing**: Simultaneous Google + Bing requests
- **🎯 SaaS Ready**: Perfect for real-time user onboarding
- **📊 Smart Limiting**: 3-5 keywords for speed (expandable)
- **💼 Business Model**: Freemium → Premium upsell path

## ✨ Features

### Core AI Visibility Tracking
- **🤖 AI Overview Tracking**: Monitor Google AI Overview presence and brand citations
- **🔍 Multi-Engine Analysis**: Google and Bing SERP analysis with AI feature detection
- **🏆 Competitor Intelligence**: Track competitor visibility in AI-generated content
- **� SERP Features**: Monitor Featured Snippets, Knowledge Graph, People Also Ask

### SaaS Integration Ready
- **⚡ Fast API Service**: REST endpoints optimized for SaaS
- **� Real-time Analysis**: 30-second user onboarding flow
- **💰 Business Intelligence**: AI visibility scoring (0-100)
- **🎯 Enhanced Insights**: People Also Ask from both engines
- **💾 Export Capabilities**: JSON export for integration

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Setup Python environment and dependencies
chmod +x setup.sh
./setup.sh
```

### 2. Configure Credentials
```bash
# Set DataForSEO credentials
export DATAFORSEO_LOGIN="your_login"
export DATAFORSEO_PASSWORD="your_password"

# Or create .env file
echo "DATAFORSEO_LOGIN=your_login" > .env
echo "DATAFORSEO_PASSWORD=your_password" >> .env
```

### 3. Test Performance (Recommended)
```bash
# Test optimized fast analysis (30-second demo)
python demos/demo_performance_optimizations.py

# Test with real API calls
python tests/performance/test_performance_improvements.py
```

### 4. Deploy Fast API for SaaS
```bash
# Deploy production-ready fast API
./deploy_fast_api.sh
```

## 📁 Organized Project Structure

### 🎯 For SaaS Integration
- **`fast_ai_visibility_monitor.py`** ⭐ **Optimized analysis engine (30s)**
- **`fast_api_service.py`** ⭐ **Production fast API service**
- **`demos/`** - Interactive demonstrations (no credentials needed)
- **`tests/performance/`** - Performance validation scripts

### 🔧 For Development
- **`tests/api/`** - API endpoint testing
- **`tests/integration/`** - Third-party service testing
- **`tests/`** - Legacy functionality tests
- **`debug/`** - Debugging tools and utilities

### 📊 Usage Examples

**Fast Analysis (SaaS Integration):**
```bash
# Demo without API calls (5 seconds)
python demos/demo_performance_optimizations.py

# Real fast analysis (30 seconds)
python tests/performance/test_performance_improvements.py

# Deploy fast API
./deploy_fast_api.sh
```

**Standard Analysis (Comprehensive):**
```bash
# Full featured analysis (2-3 minutes)
python ai_visibility_monitor.py

# API service deployment
./deploy.sh
```

## 🎯 User Journey

### Fast Analysis (SaaS Onboarding)
1. **Input**: Brand name, domain, 3-5 keywords
2. **Parallel Processing**: Simultaneous Google + Bing SERP requests
3. **Core Analysis**: AI Overview presence, brand citations, basic scoring
4. **Results**: 30-second AI readiness assessment
5. **Upsell**: Offer comprehensive analysis as premium

### Standard Analysis (Comprehensive)
1. **Input Collection**: Brand name, domain, competitors, queries, industry, location, device
2. **Keyword Discovery**: Automatically discovers additional brand keywords via DataForSEO Labs
3. **Knowledge Graph**: Fetches brand entity information from Google
4. **SERP Analysis**: 
   - Google SERP (Advanced) → Extract AI Overview citations and SERP features
   - Bing SERP (Advanced) → Extract AI features and brand visibility
5. **Competitor Analysis**: Track competitor citations in AI results
6. **Enhanced Insights**: People Also Ask questions from both engines
7. **Summary Report**: Generate comprehensive AI visibility metrics
8. **Export**: JSON results for further analysis

## API Endpoints Used

### DataForSEO Labs (Keyword Discovery)
- `keywords_for_site/live` - Discover brand keywords
- `ranked_keywords/live` - Get ranking data with SERP features

### Google SERP APIs
- `serp/google/organic/live/advanced` - Full SERP with AI Overview
- `serp/google/knowledge_graph/live` - Brand entity information

### Bing SERP APIs
- `serp/bing/organic/live/advanced` - Bing SERP with AI features

## Example Output

```
📊 AI VISIBILITY SUMMARY REPORT
==================================================
Brand: Nike
Domain: nike.com
Analysis Date: 2025-08-09 14:30:25
Keywords Analyzed: 20

🔴 GOOGLE AI OVERVIEW METRICS
AI Overview Presence: 15/20 (75.0%)
Brand Citations: 8/15 (53.3%)

🏆 COMPETITOR AI CITATIONS
  adidas.com: 12 citations
  puma.com: 8 citations
  underarmour.com: 5 citations

🔵 BING AI FEATURES
AI Features Present: 10/20 (50.0%)
Brand Visibility: 6/10 (60.0%)

📈 OTHER SERP FEATURES
Featured Snippets: 12/20 (60.0%)
Knowledge Graph: 5/20 (25.0%)
People Also Ask: 18/20 (90.0%)
```

## File Structure

```
/workspaces/data4seo-api/
├── ai_visibility_monitor.py              # Main application (CLI)
├── fast_ai_visibility_monitor.py         # ⚡ Fast analysis for SaaS (5-10x faster)
├── api_service.py                        # FastAPI web service
├── fast_api_service.py                   # 🚀 Fast API for SaaS integration
├── setup.sh                              # Setup script
├── requirements.txt                      # Python dependencies
├── config.json                           # Configuration settings
├── README.md                             # This file
├── .env.template                         # Environment variables template
├── Procfile                              # Render start command
├── render.yaml                           # Render configuration
├── build.sh / deploy.sh                  # Deployment scripts
├── docs/                                 # 📚 All documentation organized here
│   ├── README.md                         # Documentation index
│   ├── SAAS_OPTIMIZATION_GUIDE.md        # SaaS integration guide
│   ├── TESTING_PERFORMANCE_GUIDE.md      # Performance testing
│   ├── WORKSPACE_STRUCTURE.md            # Project organization
│   ├── API_DEPLOYMENT.md                 # Deployment guide
│   ├── DEPLOYMENT_SUMMARY.md             # Deployment summary
│   ├── ORGANIZATION_COMPLETE.md          # Organization achievements
│   ├── DataForSEO v3.pdf                 # API documentation
│   └── DataForSEO v3.postman_collection.json # Postman collection
├── demos/                                # 🎭 Interactive demonstrations
│   ├── README.md                         # Demo documentation
│   ├── demo_performance_optimizations.py # No-API performance demo
│   ├── simple_fast_demo.py               # Quick validation
│   └── demo.py                           # Basic functionality
├── tests/                                # 🧪 Comprehensive testing suite
│   ├── README.md                         # Test documentation
│   ├── performance/                      # Performance optimization tests
│   │   ├── test_performance_improvements.py # Main performance validation
│   │   ├── test_performance_comparison.py   # Fast vs standard comparison
│   │   ├── test_enhanced_performance.py     # Advanced performance testing
│   │   └── test_fast_monitor.py             # Direct fast monitor testing
│   ├── api/                              # API service testing
│   │   ├── test_enhanced_api.py          # Enhanced API with fast endpoints
│   │   └── test_api.py                   # Standard API testing
│   ├── integration/                      # Third-party integrations
│   │   ├── test_enhanced_insights.py     # Enhanced analytics integration
│   │   └── test_bing_paa.py              # Bing People Also Ask integration
│   └── [legacy tests]                    # Historical functionality tests
├── results/                              # 📊 Analysis output files
│   ├── README.md                         # Results documentation
│   └── *.json                           # Timestamped result files
└── debug/                                # 🐛 Debug scripts and data
    ├── README.md                         # Debug documentation
    ├── debug_*.py                        # Debug scripts
    └── debug_*.json                      # Debug output files
```

## Configuration

Edit `config.json` to customize:
- Rate limiting settings
- Default locations/languages
- Maximum keywords per analysis
- AI engine configurations

## Requirements

- Python 3.7+
- DataForSEO API account with sufficient credits
- Internet connection for API calls

## Rate Limiting

The system includes built-in rate limiting (1 second between requests) to comply with DataForSEO API guidelines. For higher throughput, adjust the delay in `config.json`.

## Export Format

Results are automatically exported to the `results/` folder with timestamp-based filenames (e.g., `results/ai_visibility_results_20250809_143025.json`).

Results are exported as JSON with the following structure:
```json
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
  "people_also_ask_present": true
}
```

## 📚 Documentation & Guides

All documentation is now organized in the **[`docs/`](docs/)** folder:

📖 **[Complete Documentation Index](docs/README.md)** - Start here for all guides  
🚀 **[SaaS Optimization Guide](docs/SAAS_OPTIMIZATION_GUIDE.md)** - 5-10x speed improvements  
🧪 **[Performance Testing Guide](docs/TESTING_PERFORMANCE_GUIDE.md)** - Benchmarking methodology  
🏗️ **[Workspace Structure](docs/WORKSPACE_STRUCTURE.md)** - Project organization  
🚀 **[API Deployment Guide](docs/API_DEPLOYMENT.md)** - Production deployment  
✅ **[Organization Complete](docs/ORGANIZATION_COMPLETE.md)** - Setup summary

## Support

For DataForSEO API documentation: https://docs.dataforseo.com/v3/

For issues with this implementation, check the console output for detailed error messages.
