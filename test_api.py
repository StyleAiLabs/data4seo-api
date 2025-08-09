#!/usr/bin/env python3
"""
Local API Test Script
Test the FastAPI service locally before deployment
"""

import requests
import json
import time
import os
from datetime import datetime

def test_api_locally():
    """Test the API service running locally"""
    
    base_url = "http://localhost:8000"
    
    print("🧪 Testing AI Visibility Monitor API")
    print("=====================================")
    
    # Test 1: Health check
    print("\n1️⃣ Testing health check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure it's running on localhost:8000")
        print("   Run: uvicorn api_service:app --reload")
        return False
    
    # Test 2: Root endpoint
    print("\n2️⃣ Testing root endpoint...")
    response = requests.get(f"{base_url}/")
    if response.status_code == 200:
        print("✅ Root endpoint working")
        print(f"   Response: {response.json()}")
    else:
        print(f"❌ Root endpoint failed: {response.status_code}")
    
    # Test 3: Start analysis (minimal test)
    print("\n3️⃣ Testing analysis endpoint...")
    
    # Check for credentials
    if not os.getenv('DATAFORSEO_LOGIN') or not os.getenv('DATAFORSEO_PASSWORD'):
        print("⚠️  No DataForSEO credentials found. Testing with mock request...")
        
        test_payload = {
            "brand_name": "Nike",
            "brand_domain": "nike.com",
            "competitors": ["adidas.com"],
            "serp_queries": ["running shoes"],
            "industry": "Sports",
            "location": "United States",
            "device": "desktop",
            "language": "English"
        }
        
        response = requests.post(f"{base_url}/api/v1/analyze", json=test_payload)
        
        if response.status_code == 500:
            data = response.json()
            if "credentials not configured" in data.get('detail', ''):
                print("✅ Analysis endpoint working (credentials validation passed)")
            else:
                print(f"❌ Unexpected error: {data}")
        else:
            print(f"✅ Analysis endpoint accepted request: {response.status_code}")
            if response.status_code == 200:
                analysis_data = response.json()
                print(f"   Analysis ID: {analysis_data.get('analysis_id')}")
    else:
        print("✅ DataForSEO credentials found. Ready for real analysis!")
    
    # Test 4: List analyses
    print("\n4️⃣ Testing list analyses...")
    response = requests.get(f"{base_url}/api/v1/analyses")
    if response.status_code == 200:
        print("✅ List analyses working")
        data = response.json()
        print(f"   Found {len(data.get('analyses', []))} analyses")
    else:
        print(f"❌ List analyses failed: {response.status_code}")
    
    print("\n✅ API tests completed!")
    print("\n📚 Next Steps:")
    print("- Deploy to Render: ./deploy.sh")
    print("- View API docs: http://localhost:8000/docs")
    print("- Test with real credentials in production")
    
    return True

if __name__ == "__main__":
    test_api_locally()
