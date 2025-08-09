# 🧪 Tests

This folder contains all test files for the AI Visibility Monitor API.

## � **Contents**

### **🔬 Core API Tests**
- `test_optimized_api.py` - Tests for the optimized single endpoint API
- `test_fast_mode_workflow.py` - Complete workflow test for fast mode functionality
- `quick_ai_test.py` - Quick AI visibility test
- `quick_brand_test.py` - Quick brand analysis test
- `quick_enhanced_test.py` - Enhanced quick test
- `quick_test.py` - Basic quick test

### **📊 Analysis Tests**
- `analyze_heart_disease_insights.py` - Healthcare industry analysis test
- `test_ai_overview_detection.py` - AI Overview detection testing
- `test_api_fixes.py` - API fixes validation

### **🎯 Business Scenario Tests**
- `test_business_scenario.py` - Real business use case testing

## 🚀 **New Optimized Tests**

### **Fast Mode Workflow Test**
```bash
python tests/test_fast_mode_workflow.py
```
Tests the complete fast mode workflow:
- Analysis initiation
- Status polling  
- Results retrieval
- Performance validation

### **Optimized API Test**
```bash
python tests/test_optimized_api.py
```
Tests both fast and comprehensive modes of the optimized API.

## 🎯 **Test Categories**

| Category | Files | Purpose |
|----------|-------|---------|
| **API Tests** | `test_optimized_api.py`, `test_fast_mode_workflow.py` | Test optimized API functionality |
| **Quick Tests** | `quick_*.py` | Fast validation tests |
| **Analysis Tests** | `test_ai_*.py`, `analyze_*.py` | Deep analysis validation |
| **Business Tests** | `test_business_scenario.py` | Real-world use case testing |

## ▶️ **Running Tests**

### **Run All Tests**
```bash
# From project root
python -m pytest tests/
```

### **Run Specific Test**
```bash
python tests/test_optimized_api.py
```

### **Run Quick Tests Only**
```bash
python tests/quick_test.py
```

## 🔧 **Test Requirements**

- DataForSEO API credentials in `.env` file
- Active internet connection
- Python dependencies installed (`pip install -r requirements.txt`)

## 📊 **Test Results**

Tests validate:
- API response format and structure
- Performance metrics and timing
- AI Overview detection accuracy
- Brand citation analysis
- Error handling and edge cases
