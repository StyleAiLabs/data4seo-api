# Integration Tests

This folder contains integration tests for advanced features and third-party service integrations.

## 📁 Integration Test Scripts

### `test_bing_paa.py`
**Purpose:** Bing People Also Ask (PAA) integration testing
- 🔵 Tests Bing SERP PAA extraction
- 📊 Validates PAA question formatting
- 🔄 Tests both string and dict PAA formats
- ⚡ Performance validation for Bing integration
- 🔑 **Requires DataForSEO credentials**

**Usage:**
```bash
python test_bing_paa.py
```

### `test_enhanced_insights.py`
**Purpose:** Enhanced insights and analytics integration
- 📈 AI visibility scoring system testing
- 🏆 Competitor analysis integration
- 📊 PAA insights from both Google and Bing
- 🎯 Enhanced response format validation
- 💼 SaaS analytics integration testing
- 🔑 **Requires DataForSEO credentials**

**Usage:**
```bash
python test_enhanced_insights.py
```

## 🔗 Integration Features Tested

### Bing Integration
- **PAA Extraction:** People Also Ask questions from Bing SERP
- **AI Feature Detection:** Bing AI-powered search features
- **Brand Visibility:** Brand presence in Bing AI results
- **Data Normalization:** Consistent format across engines

### Analytics Integration
- **AI Visibility Scoring:** 0-100 scale scoring system
- **Competitor Analysis:** Multi-brand comparison
- **PAA Insights:** Question analysis from both engines
- **Performance Metrics:** Processing time and efficiency

## 📊 Integration Test Coverage

| Integration | Test Script | Coverage |
|-------------|-------------|----------|
| **Bing PAA** | `test_bing_paa.py` | PAA extraction, formatting, performance |
| **Enhanced Analytics** | `test_enhanced_insights.py` | Scoring, competitors, insights |

## 🎯 Test Scenarios

### Bing PAA Testing
1. **Standard PAA Format:** Array of question strings
2. **Complex PAA Format:** Objects with question/snippet data
3. **Mixed Format Handling:** Both formats in same response
4. **Performance Testing:** Extraction speed validation

### Enhanced Insights Testing
1. **AI Scoring Algorithm:** Accurate 0-100 scoring
2. **Competitor Comparison:** Multi-brand analysis
3. **Cross-Engine PAA:** Google + Bing question insights
4. **Response Enhancement:** Complete data integration

## 🔧 Integration Validation

### Before Running Tests
1. Ensure DataForSEO credentials are configured
2. Verify internet connectivity
3. Check API credit availability

### Test Execution
```bash
# Test Bing PAA integration
python test_bing_paa.py

# Test enhanced insights
python test_enhanced_insights.py
```

### Expected Results
- ✅ Successful PAA extraction from Bing
- ✅ Accurate AI visibility scoring
- ✅ Proper competitor analysis
- ✅ Enhanced response formatting
- ✅ Performance within acceptable limits

## 🚀 Integration Benefits

**For SaaS Applications:**
- **Comprehensive Insights:** Data from multiple search engines
- **Rich Analytics:** Advanced scoring and competitor analysis
- **User Value:** More actionable insights for customers
- **Competitive Advantage:** Unique multi-engine analysis

**For Business Intelligence:**
- **Market Analysis:** Cross-platform visibility tracking
- **Trend Detection:** PAA question trending analysis
- **Performance Benchmarking:** Competitor comparison metrics
- **Strategic Insights:** Data-driven decision making

All integration tests ensure seamless third-party service integration and enhanced analytics capabilities for production deployment.
