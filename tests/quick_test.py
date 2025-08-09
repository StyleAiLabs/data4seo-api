#!/usr/bin/env python3
"""
Quick test script for DataForSEO API integration
"""

import requests
import json
import os

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

def test_dataforseo_connection():
    """Test DataForSEO API connection"""
    login = os.getenv('DATAFORSEO_LOGIN', 'test_login')
    password = os.getenv('DATAFORSEO_PASSWORD', 'test_password')
    
    # Test Google SERP Live Advanced
    url = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"
    
    payload = [{
        "keyword": "AI search",
        "location_name": "United States",
        "language_name": "English",
        "device": "desktop"
    }]
    
    try:
        response = requests.post(
            url,
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Connection successful!")
            
            # Check for AI Overview
            if data.get('tasks') and data['tasks'][0].get('result'):
                items = data['tasks'][0]['result'][0].get('items', [])
                ai_overview_found = any(item.get('type') == 'ai_overview' for item in items)
                print(f"🤖 AI Overview found: {ai_overview_found}")
                
                # Print SERP feature types
                feature_types = [item.get('type') for item in items]
                print(f"📊 SERP features: {set(feature_types)}")
            
        elif response.status_code == 401:
            print("❌ Authentication failed - check credentials")
        else:
            print(f"❌ Request failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_dataforseo_connection()
