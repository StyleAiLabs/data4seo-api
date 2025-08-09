#!/usr/bin/env python3
"""
Test the task-based DataForSEO API implementation
"""

import requests
import json
import os
import time

# Load environment variables from .env file if it exists
def load_env():
    """Load environment variables from .env file"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env()

def test_task_based_api():
    """Test the task-based DataForSEO API approach"""
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ No credentials found")
        return
    
    base_url = "https://api.dataforseo.com/v3"
    
    print("🧪 Testing Task-Based DataForSEO API")
    print("="*40)
    
    # Test Google SERP task-based approach
    print("\n1. Testing Google SERP Task-Based Approach...")
    
    try:
        # Step 1: Post task
        post_url = f"{base_url}/serp/google/organic/task_post"
        payload = [{
            "keyword": "AI search",
            "location_code": 2840,  # United States
            "language_code": "en",   # English
            "device": "desktop"
        }]
        
        print("   📤 Posting task...")
        response = requests.post(
            post_url,
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        if response.status_code == 200:
            task_data = response.json()
            print(f"   ✅ Task posted successfully!")
            
            if task_data.get('tasks') and task_data['tasks'][0].get('id'):
                task_id = task_data['tasks'][0]['id']
                print(f"   📋 Task ID: {task_id}")
                
                # Step 2: Check task status
                print("   ⏳ Waiting for task completion...")
                
                max_wait = 30
                wait_time = 0
                task_ready = False
                
                while wait_time < max_wait:
                    # Check if task is ready
                    ready_url = f"{base_url}/serp/google/organic/tasks_ready"
                    ready_response = requests.get(ready_url, auth=(login, password))
                    
                    if ready_response.status_code == 200:
                        ready_data = ready_response.json()
                        
                        if ready_data.get('tasks'):
                            for task in ready_data['tasks']:
                                if task.get('id') == task_id:
                                    task_ready = True
                                    print(f"   ✅ Task {task_id} is ready!")
                                    break
                    
                    if task_ready:
                        break
                    
                    time.sleep(2)
                    wait_time += 2
                    print(f"   ⏳ Still waiting... ({wait_time}s)")
                
                if task_ready:
                    # Step 3: Get results
                    get_url = f"{base_url}/serp/google/organic/task_get/advanced/{task_id}"
                    print(f"   📥 Fetching results from: {get_url}")
                    
                    result_response = requests.get(get_url, auth=(login, password))
                    
                    if result_response.status_code == 200:
                        result_data = result_response.json()
                        print("   ✅ Results retrieved successfully!")
                        
                        if result_data.get('tasks') and result_data['tasks'][0].get('result'):
                            items = result_data['tasks'][0]['result'][0].get('items', [])
                            print(f"   📊 Found {len(items)} SERP items")
                            
                            # Check for AI Overview
                            ai_overview_found = any(item.get('type') == 'ai_overview' for item in items)
                            print(f"   🤖 AI Overview found: {ai_overview_found}")
                            
                            # Show SERP feature types
                            feature_types = list(set(item.get('type') for item in items))
                            print(f"   📈 SERP features: {feature_types[:10]}")  # Limit output
                        else:
                            print("   ⚠️  No results in response")
                    else:
                        print(f"   ❌ Failed to get results: {result_response.status_code}")
                        print(f"   📝 Response: {result_response.text[:200]}")
                else:
                    print(f"   ⏰ Task did not complete within {max_wait} seconds")
            else:
                print("   ❌ No task ID in response")
                print(f"   📝 Response: {task_data}")
        else:
            print(f"   ❌ Failed to post task: {response.status_code}")
            print(f"   📝 Response: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Error during task-based test: {e}")

if __name__ == "__main__":
    test_task_based_api()
