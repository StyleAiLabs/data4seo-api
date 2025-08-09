# Tests Directory

This directory contains all test scripts for the AI Visibility Monitor.

## Test Files

### Core Functionality Tests
- **`test_ai_overview_detection.py`** - Tests AI Overview detection with known triggering keywords
- **`test_api_fixes.py`** - Tests API parameter fixes and validations
- **`test_business_scenario.py`** - Real business use case test (Mayo Clinic example)
- **`test_live_vs_task.py`** - Performance comparison between live and task-based APIs
- **`test_task_based_api.py`** - Tests task-based API approach

### Quick Tests
- **`quick_test.py`** - Basic API connection test
- **`quick_ai_test.py`** - Quick AI Overview test
- **`quick_brand_test.py`** - Quick brand citation test

### Demo
- **`demo.py`** - Sample data testing and demonstration

## Running Tests

To run any test, use:
```bash
cd /workspaces/data4seo-api
python3 tests/[test_file_name].py
```

Example:
```bash
python3 tests/test_business_scenario.py
```

## Requirements

All tests require:
- Valid DataForSEO credentials in `.env` file
- Python dependencies from `requirements.txt`
- Active internet connection
