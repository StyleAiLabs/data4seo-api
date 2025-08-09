#!/usr/bin/env python3
"""
Test AI Overview Detection with Keywords Known to Trigger AI Overviews
"""

import sys
import time
from ai_visibility_monitor import AIVisibilityMonitor, AIVisibilityAnalyzer

def test_ai_overview_detection():
    """Test with keywords that should trigger AI Overviews"""
    
    # Load credentials
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # Get credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ Missing credentials! Please set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD in .env file")
        return
    
    # Keywords that typically trigger AI Overviews (informational queries)
    test_keywords = [
        "what is artificial intelligence",
        "how to lose weight",
        "benefits of meditation", 
        "what is climate change",
        "how does photosynthesis work"
    ]
    
    print("🧪 Testing AI Overview Detection")
    print("=" * 50)
    
    monitor = AIVisibilityMonitor(login, password)
    
    # Configure test parameters
    monitor.brand_domain = "wikipedia.org"  # Use a domain likely to be cited
    monitor.competitor_domains = ["britannica.com", "healthline.com", "mayoclinic.com"]
    
    for keyword in test_keywords:
        print(f"\n📈 Testing: '{keyword}'")
        print("-" * 40)
        
        try:
            # Get SERP data
            serp_data = monitor.client.get_google_serp_advanced(
                keyword=keyword,
                location="United States", 
                device="desktop",
                language="English"
            )
            
            # Analyze for AI Overview
            analyzer = AIVisibilityAnalyzer("wikipedia.org", ["britannica.com", "healthline.com"])
            analysis = analyzer.analyze_google_serp(serp_data)
            
            if analysis['ai_overview_present']:
                print(f"  ✅ AI Overview detected!")
                print(f"  📊 Citations found: {len(analysis['ai_citations'])}")
                if analysis['ai_citations']:
                    print(f"  🔗 Cited domains: {', '.join(analysis['ai_citations'][:5])}")  # Show first 5
                if analysis['brand_cited']:
                    print(f"  🎯 Brand cited: YES")
                else:
                    print(f"  ❌ Brand not cited")
            else:
                print(f"  ❌ No AI Overview found")
                
            # Add delay to respect rate limits
            time.sleep(1)
            
        except Exception as e:
            print(f"  💥 Error: {e}")
    
    print(f"\n🏁 Test completed!")

if __name__ == "__main__":
    test_ai_overview_detection()
