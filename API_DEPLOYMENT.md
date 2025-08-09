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

### **Base URL**
```
https://your-service-name.onrender.com
```

### **Authentication**
No API key required. DataForSEO credentials are configured server-side.

---

## 🔗 **Endpoints**

### **1. Health Check**
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

### **2. Start Analysis**
```http
POST /api/v1/analyze
Content-Type: application/json
```

**Request Body:**
```json
{
  "brand_name": "Nike",
  "brand_domain": "nike.com",
  "competitors": ["adidas.com", "puma.com"],
  "serp_queries": ["running shoes", "athletic wear", "sneakers"],
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

### **3. Get Analysis Status**
```http
GET /api/v1/analysis/{analysis_id}/status
```

**Response:**
```json
{
  "analysis_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running",
  "progress": 2,
  "message": "Analysis running",
  "started_at": "2025-08-09T14:30:25"
}
```

**Status Values:**
- `pending` - Analysis queued
- `running` - Analysis in progress
- `completed` - Analysis finished successfully
- `failed` - Analysis encountered an error

### **4. Get Analysis Results**
```http
GET /api/v1/analysis/{analysis_id}
```

**Response:**
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
    "location": "United States",
    "device": "desktop",
    "language": "English"
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
        "How often should you replace running shoes?",
        "What's the difference between road and trail running shoes?"
      ],
      "bing_people_also_ask_present": true,
      "bing_people_also_ask_queries": [
        "running shoes for flat feet",
        "best running shoes 2025",
        "running shoes vs walking shoes"
      ],
      "ai_visibility_score": 85.0,
      "competitor_ai_scores": {"adidas.com": 70.0, "puma.com": 45.0},
      "ai_dominance_rank": 1
    }
  ],
  "summary": {
    "total_queries": 1,
    "ai_overview_presence": {
      "count": 1,
      "percentage": 100.0
    },
    "brand_citations": {
      "count": 1,
      "percentage": 100.0
    },
    "ai_visibility_scoring": {
      "average_score": 85.0,
      "max_score": 100.0
    },
    "people_also_ask_insights": {
      "google_paa": {
        "queries_with_paa": 1,
        "total_questions": 3,
        "percentage": 100.0
      },
      "bing_paa": {
        "queries_with_paa": 1,
        "total_questions": 3,
        "percentage": 100.0
      },
      "combined_insights": {
        "total_questions": 6,
        "engines_with_paa": 2
      }
    },
    "competitor_analysis": {
      "competitor_citations": {"adidas.com": 1},
      "competitors_found": 1
    }
  },
  "started_at": "2025-08-09T14:30:25",
  "completed_at": "2025-08-09T14:32:15"
}
```

### **5. List All Analyses**
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
      "started_at": "2025-08-09T14:30:25",
      "completed_at": "2025-08-09T14:32:15"
    }
  ]
}
```

---

## 🔧 **Usage Examples**

### **cURL Examples**

**Start Analysis:**
```bash
curl -X POST "https://your-service.onrender.com/api/v1/analyze" \
     -H "Content-Type: application/json" \
     -d '{
       "brand_name": "Nike",
       "brand_domain": "nike.com",
       "competitors": ["adidas.com"],
       "serp_queries": ["running shoes"],
       "industry": "Sports",
       "location": "United States",
       "device": "desktop",
       "language": "English"
     }'
```

**Check Status:**
```bash
curl "https://your-service.onrender.com/api/v1/analysis/ANALYSIS_ID/status"
```

**Get Results:**
```bash
curl "https://your-service.onrender.com/api/v1/analysis/ANALYSIS_ID"
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

- **Swagger UI**: `https://your-service.onrender.com/docs`
- **ReDoc**: `https://your-service.onrender.com/redoc`

---

## ⚡ **Performance Notes**

- **Analysis Time**: 2-5 minutes per keyword (depends on API response time)
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
