#!/usr/bin/env python3
"""
Debug Brand Citation Detection - Check why Mayo Clinic citation is not detected
"""

import json
from ai_visibility_monitor import DataForSEOClient, AIVisibilityAnalyzer
import os
from dotenv import load_dotenv

def debug_brand_citation():
    """Debug the specific case where Mayo Clinic should be cited but isn't detected"""
    
    load_dotenv()
    
    # Get credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ Missing credentials!")
        return
    
    print("🔍 Debugging Brand Citation Detection")
    print("=" * 50)
    
    # Test the specific query
    keyword = "heart disease symptoms"
    brand_domain = "mayoclinic.org"
    
    print(f"🔎 Analyzing: '{keyword}'")
    print(f"🎯 Looking for brand: '{brand_domain}'")
    print("-" * 40)
    
    # Get SERP data
    client = DataForSEOClient(login, password)
    serp_data = client.get_google_serp_advanced(
        keyword=keyword,
        location="United States",
        device="desktop", 
        language="English"
    )
    
    # Find AI Overview items
    if not serp_data.get('tasks') or not serp_data['tasks'][0].get('result'):
        print("❌ No SERP data found")
        return
    
    items = serp_data['tasks'][0]['result'][0].get('items', [])
    ai_overviews = [item for item in items if item.get('type') == 'ai_overview']
    
    if not ai_overviews:
        print("❌ No AI Overview found")
        return
    
    print(f"✅ Found {len(ai_overviews)} AI Overview(s)")
    
    # Examine each AI Overview in detail
    for i, overview in enumerate(ai_overviews):
        print(f"\n🤖 AI Overview #{i+1}:")
        print(f"   📋 Available keys: {list(overview.keys())}")
        
        # Check all possible citation fields
        citation_sources = []
        
        # Check 'references' field
        if 'references' in overview and overview['references']:
            print(f"   📚 References found: {len(overview['references'])}")
            for j, ref in enumerate(overview['references']):
                print(f"      {j+1}. {ref}")
                if 'url' in ref:
                    citation_sources.append(ref['url'])
                if 'domain' in ref:
                    citation_sources.append(ref['domain'])
        
        # Check 'items' field  
        if 'items' in overview and overview['items']:
            print(f"   📋 Items found: {len(overview['items'])}")
            for j, item in enumerate(overview['items']):
                print(f"      {j+1}. {item}")
                if 'url' in item:
                    citation_sources.append(item['url'])
                if 'domain' in item:
                    citation_sources.append(item['domain'])
        
        # Check 'links' field (legacy)
        if 'links' in overview and overview['links']:
            print(f"   🔗 Links found: {len(overview['links'])}")
            for j, link in enumerate(overview['links']):
                print(f"      {j+1}. {link}")
                if 'url' in link:
                    citation_sources.append(link['url'])
                if 'domain' in link:
                    citation_sources.append(link['domain'])
        
        # Check markdown content for domain mentions
        if 'markdown' in overview and overview['markdown']:
            print(f"   📝 Markdown content length: {len(overview['markdown'])} characters")
            markdown_content = overview['markdown'].lower()
            if 'mayoclinic' in markdown_content or 'mayo clinic' in markdown_content:
                print(f"   🎯 Mayo Clinic mentioned in markdown content!")
        
        print(f"\n🔍 All citation sources found:")
        for source in citation_sources:
            print(f"   - {source}")
            if isinstance(source, str):
                if 'mayoclinic' in source.lower():
                    print(f"     🎯 MAYO CLINIC MATCH FOUND!")
    
    # Test our current analyzer logic
    print(f"\n🧪 Testing Current Analyzer Logic:")
    analyzer = AIVisibilityAnalyzer(brand_domain, [])
    analysis = analyzer.analyze_google_serp(serp_data)
    
    print(f"   AI Overview Present: {analysis['ai_overview_present']}")
    print(f"   Brand Cited: {analysis['brand_cited']}")
    print(f"   AI Citations: {analysis['ai_citations']}")
    
    # Save debug data
    debug_file = f"debug_brand_citation_{keyword.replace(' ', '_')}.json"
    with open(debug_file, 'w') as f:
        json.dump(ai_overviews, f, indent=2)
    print(f"\n💾 Debug data saved to: {debug_file}")

if __name__ == "__main__":
    debug_brand_citation()
