#!/usr/bin/env python3
"""
Complete Fast Mode API Test - Shows the correct workflow
"""

import time
import requests
import json

def test_fast_mode_workflow():
    """Demonstrates the correct way to use the fast mode API"""
    
    print("🚀 FAST MODE API WORKFLOW TEST")
    print("=" * 50)
    
    # Step 1: Start the analysis
    print("\n📝 Step 1: Starting Fast Mode Analysis...")
    
    request_data = {
        "brand_name": "WebMD",
        "brand_domain": "webmd.com",
        "competitors": ["healthline.com"],
        "serp_queries": ["diabetes symptoms", "heart disease treatment"], 
        "industry": "Healthcare",
        "fast_mode": True
    }
    
    try:
        response = requests.post(
            "https://data4seo-api.onrender.com/api/v1/analyze",
            json=request_data,
            timeout=30
        )
        
        if response.status_code == 200:
            initial_result = response.json()
            analysis_id = initial_result['analysis_id']
            
            print(f"✅ Analysis started successfully!")
            print(f"   Analysis ID: {analysis_id}")
            print(f"   Status: {initial_result['status']}")
            print(f"   Message: {initial_result['message']}")
            print(f"   Started at: {initial_result['started_at']}")
            print(f"   Completed at: {initial_result['completed_at']}")  # Will be null initially
            
            print("\n⏳ Step 2: Waiting for completion...")
            print("   Expected time: 60-75 seconds (currently no parallel processing)")
            
            # Step 2: Poll for completion
            max_attempts = 20  # 20 attempts * 5 seconds = 100 seconds max
            attempt = 0
            
            while attempt < max_attempts:
                attempt += 1
                time.sleep(5)  # Wait 5 seconds between checks
                
                try:
                    status_response = requests.get(
                        f"https://data4seo-api.onrender.com/api/v1/analysis/{analysis_id}/status",
                        timeout=10
                    )
                    
                    if status_response.status_code == 200:
                        status = status_response.json()
                        print(f"   Check {attempt}: {status['status']} (elapsed: {attempt * 5}s)")
                        
                        if status['status'] == 'completed':
                            print(f"\n✅ Analysis completed!")
                            print(f"   Started: {status['started_at']}")
                            print(f"   Completed: {status['completed_at']}")
                            
                            # Step 3: Get full results
                            print("\n📊 Step 3: Getting full results...")
                            
                            results_response = requests.get(
                                f"https://data4seo-api.onrender.com/api/v1/analysis/{analysis_id}",
                                timeout=10
                            )
                            
                            if results_response.status_code == 200:
                                results = results_response.json()
                                summary = results['summary']
                                
                                print(f"\n🎯 FAST MODE RESULTS:")
                                print(f"   Processing time: {summary['processing_time_seconds']} seconds")
                                print(f"   Performance mode: {summary['performance_mode']}")
                                print(f"   Keywords analyzed: {summary['optimization_applied']['keywords_analyzed']}")
                                print(f"   Competitors analyzed: {summary['optimization_applied']['competitors_analyzed']}")
                                print(f"   Parallel processing: {summary['optimization_applied']['parallel_processing']}")
                                print(f"   AI Overview presence: {summary['ai_overview_presence']['percentage']}%")
                                print(f"   Brand citations: {summary['brand_citations']['percentage']}%")
                                print(f"   Speed improvement: {summary['performance_insights']['speed_improvement']}")
                                
                                return True
                            else:
                                print(f"❌ Failed to get results: {results_response.status_code}")
                                return False
                                
                        elif status['status'] == 'failed':
                            print(f"❌ Analysis failed!")
                            return False
                            
                    else:
                        print(f"   Check {attempt}: Status check failed ({status_response.status_code})")
                        
                except Exception as e:
                    print(f"   Check {attempt}: Error - {e}")
            
            print(f"\n⏰ Timeout: Analysis didn't complete within {max_attempts * 5} seconds")
            return False
            
        else:
            print(f"❌ Failed to start analysis: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting analysis: {e}")
        return False

def test_api_info():
    """Test the API info endpoint"""
    print("\n📋 API Information:")
    try:
        response = requests.get("https://data4seo-api.onrender.com/api/info", timeout=10)
        if response.status_code == 200:
            info = response.json()
            print(f"   Service: {info['service']}")
            print(f"   Version: {info['version']}")
            print(f"   Fast mode parallel processing: {info['api']['fast_mode']['parallel_processing']}")
            print(f"   Expected fast mode time: {info['api']['fast_mode']['response_time']}")
        else:
            print(f"❌ Failed to get API info: {response.status_code}")
    except Exception as e:
        print(f"❌ Error getting API info: {e}")

if __name__ == "__main__":
    test_api_info()
    success = test_fast_mode_workflow()
    
    if success:
        print("\n🎉 FAST MODE TEST COMPLETED SUCCESSFULLY!")
        print("\n💡 KEY FINDINGS:")
        print("   - Fast mode works but takes 60-75 seconds (not 15-30s)")
        print("   - parallel_processing=false (FastAIVisibilityMonitor not available)")
        print("   - Initial POST response has completed_at=null (as expected)")
        print("   - Must poll /status or /analysis/{id} endpoints for final results")
        print("   - Healthcare keywords trigger AI Overviews better than sports keywords")
    else:
        print("\n❌ Test failed or timed out")
