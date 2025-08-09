# Debug Directory

This directory contains debug scripts and output files used during development and troubleshooting.

## Debug Scripts

### Core Issue Investigation
- **`debug_brand_citation.py`** - Investigates brand citation detection issues
- **`debug_domain_matching.py`** - Tests domain matching logic
- **`debug_serp.py`** - Analyzes SERP response structure and AI Overview detection

### Main Script Debugging
- **`debug_main_script.py`** - Tests main script flow in isolation
- **`debug_main_minimal.py`** - Minimal test of main script
- **`debug_original_scenario.py`** - Tests original business scenario with timeout

## Debug Output Files

### SERP Response Data
- **`debug_serp_*.json`** - Raw SERP responses for specific keywords:
  - `debug_serp_best_running_shoes.json`
  - `debug_serp_ChatGPT.json` 
  - `debug_serp_AI_search.json`

### Brand Citation Analysis
- **`debug_brand_citation_heart_disease_symptoms.json`** - Detailed AI Overview data for brand citation investigation

## Usage

These files were used to:
1. 🐛 **Identify Issues**: Domain matching bugs, AI Overview structure changes
2. 🔧 **Develop Fixes**: Test domain cleaning logic, citation extraction
3. ✅ **Verify Solutions**: Confirm fixes work correctly

## Historical Context

Key issues resolved:
- ❌ **Domain Matching Bug**: `www.mayoclinic.org` vs `mayoclinic.org` comparison failure
- ❌ **AI Overview Structure**: Using wrong fields (`links` vs `references`/`items`)
- ✅ **Citation Detection**: Now correctly identifies brand citations in AI Overviews

## Note

These files are kept for reference and future debugging. Most issues have been resolved and fixes applied to the main script.
