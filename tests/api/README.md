# API Tests

This folder contains API testing scripts for both the standard and fast API services.

## 📁 API Test Scripts

### `test_api.py`
**Purpose:** Standard API service testing
- 🔄 Tests complete analysis workflow
- 📊 Background task processing validation
- 🎯 Full feature testing (20+ keywords)
- ⏱️ Tests 2-3 minute comprehensive analysis
- 🔑 **Requires DataForSEO credentials**

**Usage:**
```bash
python test_api.py
```

### `test_enhanced_api.py` ⭐ **Latest**
**Purpose:** Enhanced API service with all new features
- 🚀 Tests fast analysis endpoints
- ⚡ Bing PAA integration testing
- 📈 AI visibility scoring validation
- 🎯 Competitor analysis testing
- 💼 SaaS onboarding endpoint testing
- 🔑 **Requires DataForSEO credentials**

**Usage:**
```bash
python test_enhanced_api.py
```

## 🌐 API Endpoints Tested

### Standard API (`api_service.py`)
- `POST /api/v1/analyze` - Start comprehensive analysis
- `GET /api/v1/analysis/{id}` - Get analysis results
- `GET /api/v1/analysis/{id}/status` - Check analysis status
- `GET /api/v1/analyses` - List all analyses

### Fast API (`fast_api_service.py`)
- `POST /api/v2/onboarding-analysis` - Ultra-fast 30-second analysis
- `POST /api/v2/fast-analysis` - Detailed fast analysis
- `POST /api/v2/batch-onboarding` - Multi-brand processing
- `GET /api/v2/performance-metrics` - API performance data

## 📊 API Performance Comparison

| API Service | Response Time | Use Case | Features |
|-------------|---------------|----------|----------|
| **Standard API** | 2-3 minutes | Comprehensive reports | 20+ keywords, full analysis |
| **Fast API** | 15-30 seconds | SaaS onboarding | 3-5 keywords, core metrics |

## 🔧 Testing Process

### 1. Start API Service
```bash
# For standard API
python api_service.py

# For fast API  
python fast_api_service.py
```

### 2. Run Tests
```bash
# Test standard API
python test_api.py

# Test enhanced/fast API
python test_enhanced_api.py
```

### 3. Validate Results
- ✅ Check response times
- ✅ Verify AI visibility scores
- ✅ Validate data completeness
- ✅ Test error handling

## 🎯 Integration Testing

These API tests validate:
- **Real-time Performance:** 30-second response times
- **Data Accuracy:** Correct AI visibility metrics
- **Error Handling:** Graceful failure management
- **Scalability:** Multiple concurrent requests
- **SaaS Readiness:** Production deployment validation

## 🚀 Production Deployment

After successful API testing:
1. Deploy using `deploy_fast_api.sh`
2. Monitor performance with `/api/v2/performance-metrics`
3. Integrate with SaaS onboarding flow
4. Set up monitoring and alerting

All API tests ensure the services are ready for production SaaS integration.
