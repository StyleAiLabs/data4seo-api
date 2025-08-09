# Results Directory

This directory contains output files from AI Visibility Monitor analyses.

## File Naming Convention

Results are automatically saved with timestamp-based filenames:
```
ai_visibility_results_YYYYMMDD_HHMMSS.json
```

Example: `ai_visibility_results_20250809_143025.json`

## File Contents

Each result file contains a JSON array of analysis results with the following structure:

```json
[
  {
    "query": "heart disease symptoms",
    "location": "United States",
    "device": "desktop", 
    "timestamp": "2025-08-09T14:30:25",
    "google_ai_overview_present": true,
    "google_brand_cited": true,
    "google_ai_citations": ["www.mayoclinic.org", "www.healthline.com"],
    "google_competitor_citations": {"healthline.com": 1},
    "bing_ai_features": [],
    "bing_brand_visibility": false,
    "featured_snippet_present": false,
    "knowledge_graph_present": true,
    "people_also_ask_present": true
  }
]
```

## Data Fields

### Core Analysis
- **`query`**: Search keyword analyzed
- **`location`**: Geographic location (e.g., "United States")
- **`device`**: Device type (desktop, mobile, tablet)
- **`timestamp`**: Analysis timestamp (ISO format)

### Google AI Overview Metrics
- **`google_ai_overview_present`**: Boolean - AI Overview detected
- **`google_brand_cited`**: Boolean - Brand cited in AI Overview
- **`google_ai_citations`**: Array - All domains cited in AI Overview
- **`google_competitor_citations`**: Object - Competitor citation counts

### Bing AI Features
- **`bing_ai_features`**: Array - AI features detected (answer_box, etc.)
- **`bing_brand_visibility`**: Boolean - Brand visible in AI features

### Traditional SERP Features
- **`featured_snippet_present`**: Boolean - Featured snippet detected
- **`knowledge_graph_present`**: Boolean - Knowledge graph detected  
- **`people_also_ask_present`**: Boolean - People Also Ask detected

## Usage

These files can be:
- 📊 **Imported** into analytics tools (Excel, Tableau, etc.)
- 📈 **Processed** for trend analysis and reporting
- 🔄 **Compared** across time periods for performance tracking
- 📋 **Shared** with stakeholders for visibility insights

## Integration

To programmatically process results:

```python
import json

# Load results
with open('results/ai_visibility_results_20250809_143025.json', 'r') as f:
    results = json.load(f)

# Calculate metrics
total_queries = len(results)
ai_overview_count = sum(1 for r in results if r['google_ai_overview_present'])
brand_citation_count = sum(1 for r in results if r['google_brand_cited'])

print(f"AI Overview Coverage: {ai_overview_count}/{total_queries}")
print(f"Brand Citation Rate: {brand_citation_count}/{ai_overview_count}")
```
