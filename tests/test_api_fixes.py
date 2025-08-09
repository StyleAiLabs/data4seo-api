#!/usr/bin/env python3
"""
Test script to verify DataForSEO API fixes
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

def test_api_endpoints():
    """Test various DataForSEO API endpoints with correct parameters"""
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ No credentials found")
        return
    
    base_url = "https://api.dataforseo.com/v3"
    
    print("🧪 Testing DataForSEO API Endpoints")
    print("="*40)
    
    # Test 1: Get available locations
    print("\n1. Testing Available Locations...")
    try:
        response = requests.get(
            f"{base_url}/serp/google/locations",
            auth=(login, password)
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Locations API working - Found {len(data.get('tasks', [{}])[0].get('result', []))} locations")
            # Show a few examples
            locations = data.get('tasks', [{}])[0].get('result', [])[:5]
            for loc in locations:
                print(f"   📍 {loc.get('location_name')}: {loc.get('location_code')}")
        else:
            print(f"❌ Locations API failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Locations API error: {e}")
    
    # Test 2: Get available languages
    print("\n2. Testing Available Languages...")
    try:
        response = requests.get(
            f"{base_url}/serp/google/languages",
            auth=(login, password)
        )
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Languages API working - Found {len(data.get('tasks', [{}])[0].get('result', []))} languages")
            # Show a few examples
            languages = data.get('tasks', [{}])[0].get('result', [])[:5]
            for lang in languages:
                print(f"   🗣️  {lang.get('language_name')}: {lang.get('language_code')}")
        else:
            print(f"❌ Languages API failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Languages API error: {e}")
    
    # Test 3: Google SERP with correct parameters
    print("\n3. Testing Google SERP with correct parameters...")
    try:
        payload = [{
            "keyword": "AI search",
            "location_code": 2840,  # United States
            "language_code": "en",  # English
            "device": "desktop"
        }]
        
        response = requests.post(
            f"{base_url}/serp/google/organic/live/advanced",
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Google SERP API working!")
            
            if data.get('tasks') and data['tasks'][0].get('result'):
                items = data['tasks'][0]['result'][0].get('items', [])
                print(f"   📊 Found {len(items)} SERP items")
                
                # Check for AI Overview
                ai_overview_found = any(item.get('type') == 'ai_overview' for item in items)
                print(f"   🤖 AI Overview found: {ai_overview_found}")
                
                # Show SERP feature types
                feature_types = list(set(item.get('type') for item in items))
                print(f"   📈 SERP features: {feature_types}")
            else:
                print("   ⚠️  No SERP results returned")
        else:
            print(f"❌ Google SERP API failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Google SERP API error: {e}")
    
    # Test 4: DataForSEO Labs Keywords for Site
    print("\n4. Testing DataForSEO Labs Keywords for Site...")
    try:
        payload = [{
            "target": "nike.com",
            "location_code": 2840,  # United States
            "language_code": "en",  # English
            "limit": 10
        }]
        
        response = requests.post(
            f"{base_url}/dataforseo_labs/google/keywords_for_site/live",
            auth=(login, password),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Keywords for Site API working!")
            
            if data.get('tasks') and data['tasks'][0].get('result'):
                keywords = data['tasks'][0]['result']
                print(f"   🔍 Found {len(keywords)} keywords")
                
                # Show a few examples
                for i, kw in enumerate(keywords[:3]):
                    if 'keyword_info' in kw:
                        keyword = kw['keyword_info']['keyword']
                        volume = kw['keyword_info'].get('search_volume', 'N/A')
                        print(f"   📝 {keyword} (volume: {volume})")
            else:
                print("   ⚠️  No keyword results returned")
        elif response.status_code == 402:
            print("⚠️  Insufficient credits for Keywords for Site API")
        else:
            print(f"❌ Keywords for Site API failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Keywords for Site API error: {e}")

if __name__ == "__main__":
    test_api_endpoints()
