#!/usr/bin/env python3
"""
Test both live and task-based DataForSEO API approaches
"""

import requests
import json
import os
import time

# Load environment variables
def load_env():
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env()

def test_live_vs_task_api():
    """Test both live and task-based approaches"""
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ No credentials found")
        return
    
    base_url = "https://api.dataforseo.com/v3"
    
    print("🧪 Testing Live vs Task-Based DataForSEO API")
    print("="*45)
    
    payload = [{
        "keyword": "AI search",
        "location_code": 2840,
        "language_code": "en",
        "device": "desktop"
    }]
    
    # Test 1: Live Advanced Endpoint
    print("\n1. Testing Live Advanced Endpoint...")
    try:
        live_url = f"{base_url}/serp/google/organic/live/advanced"
        start_time = time.time()
        
        response = requests.post(
            live_url,
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Live API working! Response time: {end_time - start_time:.2f}s")
            
            if data.get('tasks') and data['tasks'][0].get('result'):
                items = data['tasks'][0]['result'][0].get('items', [])
                print(f"   📊 Found {len(items)} SERP items")
                
                # Check for AI Overview
                ai_overview_found = any(item.get('type') == 'ai_overview' for item in items)
                print(f"   🤖 AI Overview found: {ai_overview_found}")
        else:
            print(f"   ❌ Live API failed: {response.status_code}")
            print(f"   📝 Response: {response.text[:200]}")
            
    except Exception as e:
        print(f"   ❌ Live API error: {e}")
    
    # Test 2: Task-Based Endpoint (just posting, not waiting)
    print("\n2. Testing Task-Based Endpoint (posting only)...")
    try:
        task_url = f"{base_url}/serp/google/organic/task_post"
        start_time = time.time()
        
        response = requests.post(
            task_url,
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        end_time = time.time()
        
        if response.status_code == 200:
            task_data = response.json()
            print(f"   ✅ Task posted successfully! Response time: {end_time - start_time:.2f}s")
            
            if task_data.get('tasks') and task_data['tasks'][0].get('id'):
                task_id = task_data['tasks'][0]['id']
                print(f"   📋 Task ID: {task_id}")
                print(f"   💰 Cost: {task_data['tasks'][0].get('cost', 'N/A')}")
        else:
            print(f"   ❌ Task API failed: {response.status_code}")
            print(f"   📝 Response: {response.text[:200]}")
            
    except Exception as e:
        print(f"   ❌ Task API error: {e}")

if __name__ == "__main__":
    test_live_vs_task_api()
