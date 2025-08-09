#!/usr/bin/env python3
"""
Debug script to examine actual SERP response structure
"""

import requests
import json
import os

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

def debug_serp_response():
    """Debug the actual SERP response to understand AI Overview structure"""
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ No credentials found")
        return
    
    base_url = "https://api.dataforseo.com/v3"
    
    print("🔍 Debugging SERP Response Structure")
    print("="*40)
    
    # Test with a keyword that should definitely have AI Overview
    keywords_to_test = [
        "what is artificial intelligence",
        "how to lose weight",
        "best running shoes",
        "AI search",
        "ChatGPT"
    ]
    
    for keyword in keywords_to_test:
        print(f"\n📈 Testing keyword: '{keyword}'")
        
        payload = [{
            "keyword": keyword,
            "location_code": 2840,  # United States
            "language_code": "en",
            "device": "desktop"
        }]
        
        try:
            # Test Google SERP
            url = f"{base_url}/serp/google/organic/live/advanced"
            response = requests.post(
                url,
                auth=(login, password),
                headers={'Content-Type': 'application/json'},
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('tasks') and data['tasks'][0].get('result'):
                    items = data['tasks'][0]['result'][0].get('items', [])
                    print(f"   📊 Total SERP items: {len(items)}")
                    
                    # Show all item types
                    item_types = {}
                    ai_overview_items = []
                    
                    for i, item in enumerate(items):
                        item_type = item.get('type', 'unknown')
                        item_types[item_type] = item_types.get(item_type, 0) + 1
                        
                        # Collect AI Overview items for detailed inspection
                        if 'ai' in item_type.lower() or 'overview' in item_type.lower():
                            ai_overview_items.append({
                                'index': i,
                                'type': item_type,
                                'title': item.get('title', 'No title'),
                                'keys': list(item.keys())
                            })
                    
                    print(f"   📋 Item types found: {dict(sorted(item_types.items()))}")
                    
                    if ai_overview_items:
                        print(f"   🤖 AI Overview items found: {len(ai_overview_items)}")
                        for ai_item in ai_overview_items:
                            print(f"      - Index {ai_item['index']}: {ai_item['type']} - {ai_item['title']}")
                            print(f"        Keys: {ai_item['keys']}")
                    else:
                        print("   ❌ No AI Overview items found")
                        
                        # Let's check for items that might be AI-related but named differently
                        potential_ai_items = []
                        for i, item in enumerate(items):
                            item_type = item.get('type', '')
                            title = item.get('title', '')
                            
                            # Look for AI-related patterns
                            if any(keyword in item_type.lower() for keyword in ['ai', 'answer', 'summary', 'generated']):
                                potential_ai_items.append({
                                    'index': i,
                                    'type': item_type,
                                    'title': title
                                })
                        
                        if potential_ai_items:
                            print("   🔍 Potential AI-related items:")
                            for item in potential_ai_items:
                                print(f"      - Index {item['index']}: {item['type']} - {item['title']}")
                        
                        # Save first few items to a file for inspection
                        debug_file = f"debug_serp_{keyword.replace(' ', '_')}.json"
                        with open(debug_file, 'w') as f:
                            json.dump({
                                'keyword': keyword,
                                'total_items': len(items),
                                'first_10_items': items[:10]
                            }, f, indent=2)
                        print(f"   💾 First 10 items saved to: {debug_file}")
                
                else:
                    print("   ❌ No results in response")
            else:
                print(f"   ❌ Request failed: {response.status_code}")
                print(f"   📝 Response: {response.text[:200]}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        # Don't overwhelm the API
        import time
        time.sleep(1)

if __name__ == "__main__":
    debug_serp_response()
