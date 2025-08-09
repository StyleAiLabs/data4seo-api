#!/usr/bin/env python3
"""
Test the optimized API service with fast and comprehensive modes
"""

import requests
import json
import time

# Test the optimized analyze endpoint
def test_optimized_api():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing Optimized API Service")
    print("=" * 50)
    
    # Test 1: API Info
    print("\n1. Testing API Info...")
    try:
        response = requests.get(f"{base_url}/api/info", timeout=10)
        if response.status_code == 200:
            info = response.json()
            print(f"✅ Service: {info['service']}")
            print(f"✅ Version: {info['version']}")
            print(f"✅ Fast Mode Available: {info['api']['fast_mode']['parallel_processing']}")
        else:
            print(f"❌ API Info failed: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ API Info error: {e}")
        return
    
    # Test 2: Fast Mode Analysis
    print("\n2. Testing Fast Mode Analysis...")
    fast_request = {
        "brand_name": "Nike",
        "brand_domain": "nike.com",
        "competitors": ["adidas.com", "puma.com"],
        "serp_queries": ["running shoes", "athletic wear", "sports equipment"],
        "industry": "Sports",
        "fast_mode": True
    }
    
    try:
        start_time = time.time()
        response = requests.post(f"{base_url}/api/v1/analyze", json=fast_request, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Analysis started: {result['analysis_id']}")
            print(f"✅ Mode: {result['message']}")
            print(f"✅ Status: {result['status']}")
            
            # Check status
            analysis_id = result['analysis_id']
            print(f"\n   Checking status for: {analysis_id}")
            
            status_response = requests.get(f"{base_url}/api/v1/analysis/{analysis_id}/status")
            if status_response.status_code == 200:
                status = status_response.json()
                print(f"   ✅ Status: {status['status']}")
            
        else:
            print(f"❌ Fast analysis failed: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Fast analysis error: {e}")
    
    # Test 3: Comprehensive Mode Analysis
    print("\n3. Testing Comprehensive Mode Analysis...")
    comprehensive_request = {
        "brand_name": "Apple",
        "brand_domain": "apple.com", 
        "competitors": ["samsung.com", "google.com", "microsoft.com"],
        "serp_queries": ["smartphone", "tablet", "laptop", "smartwatch", "wireless earbuds"],
        "industry": "Technology",
        "fast_mode": False
    }
    
    try:
        response = requests.post(f"{base_url}/api/v1/analyze", json=comprehensive_request, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Analysis started: {result['analysis_id']}")
            print(f"✅ Mode: {result['message']}")
            print(f"✅ Status: {result['status']}")
        else:
            print(f"❌ Comprehensive analysis failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Comprehensive analysis error: {e}")
    
    # Test 4: List all analyses
    print("\n4. Testing List Analyses...")
    try:
        response = requests.get(f"{base_url}/api/v1/analyses", timeout=10)
        
        if response.status_code == 200:
            analyses = response.json()
            print(f"✅ Total analyses: {analyses['total']}")
            for analysis in analyses['analyses']:
                print(f"   - {analysis['analysis_id']}: {analysis['status']} (fast_mode: {analysis['fast_mode']})")
        else:
            print(f"❌ List analyses failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ List analyses error: {e}")
    
    print("\n🎯 Testing completed!")

if __name__ == "__main__":
    test_optimized_api()
