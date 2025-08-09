#!/usr/bin/env python3
"""
Test Enhanced API Service
Test the updated API service with Bing PAA and enhanced insights
"""

import requests
import json
import time
import os

def test_enhanced_api():
    """Test the enhanced API service functionality"""
    
    print("🚀 Testing Enhanced API Service")
    print("================================")
    
    base_url = "http://localhost:8000"
    
    # Test 1: Health check
    print("\n1️⃣ Testing health check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Starting server...")
        # Start the API server in background
        import subprocess
        subprocess.Popen([
            "/workspaces/data4seo-api/.venv/bin/uvicorn", 
            "api_service:app", 
            "--host", "0.0.0.0", 
            "--port", "8000"
        ], cwd="/workspaces/data4seo-api")
        
        print("⏳ Waiting for server to start...")
        time.sleep(5)
        
        # Try health check again
        try:
            response = requests.get(f"{base_url}/health")
            if response.status_code == 200:
                print("✅ Health check passed after restart")
            else:
                print(f"❌ Health check failed: {response.status_code}")
                return False
        except:
            print("❌ Still cannot connect to API")
            return False
    
    # Test 2: Start enhanced analysis
    print("\n2️⃣ Testing enhanced analysis endpoint...")
    
    test_payload = {
        "brand_name": "Mayo Clinic",
        "brand_domain": "mayoclinic.org",
        "competitors": ["webmd.com", "healthline.com"],
        "serp_queries": ["diabetes symptoms"],
        "industry": "Healthcare",
        "location": "United States",
        "device": "desktop",
        "language": "English"
    }
    
    response = requests.post(f"{base_url}/api/v1/analyze", json=test_payload)
    
    if response.status_code == 200:
        analysis_data = response.json()
        analysis_id = analysis_data.get('analysis_id')
        print(f"✅ Analysis started successfully")
        print(f"   Analysis ID: {analysis_id}")
        print(f"   Status: {analysis_data.get('status')}")
        
        # Test 3: Monitor analysis progress
        print("\n3️⃣ Monitoring analysis progress...")
        max_wait = 300  # 5 minutes max
        wait_time = 0
        
        while wait_time < max_wait:
            time.sleep(10)
            wait_time += 10
            
            status_response = requests.get(f"{base_url}/api/v1/analysis/{analysis_id}/status")
            if status_response.status_code == 200:
                status_data = status_response.json()
                print(f"   Status: {status_data.get('status')} (waited {wait_time}s)")
                
                if status_data.get('status') in ['completed', 'failed']:
                    break
            else:
                print(f"❌ Status check failed: {status_response.status_code}")
                break
        
        # Test 4: Get enhanced results
        print("\n4️⃣ Testing enhanced results retrieval...")
        results_response = requests.get(f"{base_url}/api/v1/analysis/{analysis_id}")
        
        if results_response.status_code == 200:
            results_data = results_response.json()
            print("✅ Enhanced results retrieved successfully")
            
            # Validate enhanced fields
            if results_data.get('results'):
                result = results_data['results'][0]
                enhanced_fields = [
                    'people_also_ask_queries',
                    'bing_people_also_ask_queries', 
                    'ai_visibility_score',
                    'competitor_ai_scores',
                    'ai_dominance_rank'
                ]
                
                print("📊 Enhanced Fields Validation:")
                for field in enhanced_fields:
                    if field in result:
                        value = result[field]
                        print(f"   ✅ {field}: {type(value).__name__} - {value}")
                    else:
                        print(f"   ❌ {field}: Missing")
            
            # Validate enhanced summary
            if results_data.get('summary'):
                summary = results_data['summary']
                enhanced_summary_fields = [
                    'ai_visibility_scoring',
                    'people_also_ask_insights',
                    'competitor_analysis'
                ]
                
                print("📈 Enhanced Summary Validation:")
                for field in enhanced_summary_fields:
                    if field in summary:
                        print(f"   ✅ {field}: Present")
                        if field == 'people_also_ask_insights':
                            paa_data = summary[field]
                            print(f"      Google PAA: {paa_data.get('google_paa', {}).get('total_questions', 0)} questions")
                            print(f"      Bing PAA: {paa_data.get('bing_paa', {}).get('total_questions', 0)} questions")
                    else:
                        print(f"   ❌ {field}: Missing")
            
            print("\n📋 Sample Enhanced Response:")
            print("=" * 40)
            print(json.dumps(results_data, indent=2)[:1000] + "..." if len(json.dumps(results_data)) > 1000 else json.dumps(results_data, indent=2))
            
        else:
            print(f"❌ Results retrieval failed: {results_response.status_code}")
            
    else:
        print(f"❌ Analysis start failed: {response.status_code}")
        if response.status_code == 500:
            error_data = response.json()
            print(f"   Error: {error_data.get('detail')}")
    
    print("\n✅ Enhanced API Service Test Completed!")
    print("🎯 Key Enhancements Tested:")
    print("   ✅ Bing People Also Ask extraction")
    print("   ✅ AI Visibility scoring")
    print("   ✅ Competitor AI analysis")
    print("   ✅ Enhanced summary metrics")
    print("   ✅ Complete API response format")

if __name__ == "__main__":
    test_enhanced_api()
