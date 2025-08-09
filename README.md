# RankAled Phase 1: AI Search Visibility Monitor

**DataForSEO V3 API Integration for Brand AI Visibility Tracking**

## Overview

This project implements a comprehensive AI search visibility monitoring system using DataForSEO APIs. It tracks brand visibility across Google AI Overviews, Bing AI features, and traditional SERP elements.

## Features

- **🤖 AI Overview Tracking**: Monitor Google AI Overview presence and brand citations
- **🔍 Multi-Engine Analysis**: Google and Bing SERP analysis with AI feature detection
- **🏆 Competitor Intelligence**: Track competitor visibility in AI-generated content
- **📊 Automated Discovery**: Discover additional brand keywords using DataForSEO Labs
- **📈 SERP Features**: Monitor Featured Snippets, Knowledge Graph, People Also Ask
- **💾 Export Capabilities**: JSON export for integration with other tools

## Quick Start

### 1. Setup
```bash
# Make setup script executable and run
chmod +x setup.sh
./setup.sh
```

### 2. Configure Credentials
```bash
export DATAFORSEO_LOGIN="your_login"
export DATAFORSEO_PASSWORD="your_password"
```

### 3. Test Connection
```bash
python3 tests/quick_test.py
```

### 4. Run Analysis

**Option A: CLI Application**
```bash
# Interactive mode
python3 ai_visibility_monitor.py

# Demo mode
python3 tests/demo.py

# Business scenario test
python3 tests/test_business_scenario.py
```

**Option B: API Service**
```bash
# Start API server
uvicorn api_service:app --reload

# Test API
python3 test_api.py

# Deploy to Render
./deploy.sh
```

## User Journey

1. **Input Collection**: Brand name, domain, competitors, queries, industry, location, device
2. **Keyword Discovery**: Automatically discovers additional brand keywords via DataForSEO Labs
3. **Knowledge Graph**: Fetches brand entity information from Google
4. **SERP Analysis**: 
   - Google SERP (Advanced) → Extract AI Overview citations and SERP features
   - Bing SERP (Advanced) → Extract AI features and brand visibility
5. **Competitor Analysis**: Track competitor citations in AI results
6. **Summary Report**: Generate comprehensive AI visibility metrics
7. **Export**: JSON results for further analysis

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
├── api_service.py                        # FastAPI web service
├── setup.sh                              # Setup script
├── requirements.txt                      # Python dependencies
├── config.json                           # Configuration settings
├── README.md                             # This file
├── API_DEPLOYMENT.md                     # API deployment guide
├── DataForSEO v3.postman_collection.json # Postman collection
├── DataForSEO v3.pdf                     # API documentation
├── Procfile                              # Render start command
├── render.yaml                           # Render configuration
├── build.sh                              # Render build script
├── deploy.sh                             # Deployment helper script
├── test_api.py                           # API testing script
├── results/                              # Analysis output files
│   ├── README.md                         # Results documentation
│   └── ai_visibility_results_*.json     # Timestamped result files
├── tests/                                # Test scripts
│   ├── README.md                         # Test documentation
│   ├── test_business_scenario.py         # Business use case tests
│   ├── test_ai_overview_detection.py     # AI Overview tests
│   ├── test_api_fixes.py                 # API validation tests
│   ├── quick_test.py                     # API connection test
│   ├── demo.py                           # Demo with sample data
│   └── ...                               # Other test files
└── debug/                                # Debug scripts and data
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

## Support

For DataForSEO API documentation: https://docs.dataforseo.com/v3/

For issues with this implementation, check the console output for detailed error messages.
