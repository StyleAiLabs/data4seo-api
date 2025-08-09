# Tests

This folder contains comprehensive test scripts for the DataForSEO AI Visibility Monitor, organized by category.

## 📁 Test Organization

### `/performance/` - Performance Testing
- **Purpose:** Speed and optimization validation
- **Scripts:** Fast vs standard analysis comparison
- **Focus:** SaaS integration readiness

### `/api/` - API Service Testing  
- **Purpose:** REST API endpoint validation
- **Scripts:** Standard and fast API testing
- **Focus:** Production deployment readiness

### `/integration/` - Integration Testing
- **Purpose:** Third-party service integration
- **Scripts:** Bing PAA, enhanced insights testing
- **Focus:** Feature completeness validation

## 📊 Legacy Test Scripts (Root Level)

### Quick Tests
- `quick_test.py` - Basic functionality test
- `quick_ai_test.py` - AI Overview detection test
- `quick_brand_test.py` - Brand citation testing
- `quick_enhanced_test.py` - Enhanced features test

### Feature Tests
- `test_ai_overview_detection.py` - AI Overview detection validation
- `test_api_fixes.py` - API parameter fixes validation
- `test_business_scenario.py` - Business use case testing
- `test_live_vs_task.py` - Live vs task-based API comparison
- `test_task_based_api.py` - Task-based API testing

### Analysis Tests
- `analyze_heart_disease_insights.py` - Specific domain analysis example

## 🎯 Test Categories Guide

| Category | Purpose | When to Use |
|----------|---------|-------------|
| **Performance** | Speed optimization validation | Before SaaS deployment |
| **API** | REST endpoint testing | Production readiness |
| **Integration** | Third-party service testing | Feature completeness |
| **Legacy** | Historical test scripts | Reference and debugging |

## 🚀 Recommended Testing Flow

1. **Start with Performance:** `tests/performance/test_performance_improvements.py`
2. **Validate API:** `tests/api/test_enhanced_api.py`
3. **Check Integrations:** `tests/integration/test_enhanced_insights.py`
4. **Quick Validation:** Use any quick_* scripts for rapid testing

## 📈 Testing for SaaS Integration

For SaaS deployment validation, prioritize:
1. Performance tests (30-second response time)
2. API endpoint tests (production readiness)
3. Integration tests (feature completeness)

All organized tests ensure the AI Visibility Monitor is production-ready for SaaS integration.

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
