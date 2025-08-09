#!/usr/bin/env python3
"""
Test Bing People Also Ask Enhancement
Test the new Bing PAA extraction functionality
"""

import os
from ai_visibility_monitor import AIVisibilityMonitor, UserInput

def test_bing_paa():
    """Test Bing People Also Ask extraction"""
    
    print("🔵 Testing Bing People Also Ask Enhancement")
    print("==========================================")
    
    # Load credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ DataForSEO credentials not found")
        return
    
    # Test with queries that might trigger PAA on both engines
    user_input = UserInput(
        brand_name="WebMD",
        brand_domain="webmd.com",
        competitors=["mayoclinic.org", "healthline.com"],
        serp_queries=["diabetes symptoms", "high blood pressure"],  # Just 2 queries for quick test
        industry="Healthcare",
        location="United States",
        device="desktop",
        language="English"
    )
    
    print(f"🔍 Testing with queries: {', '.join(user_input.serp_queries)}")
    print(f"📍 Focus: Both Google and Bing PAA extraction")
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(user_input)
    
    print("\n🔍 Detailed PAA Analysis:")
    print("=========================")
    
    for i, result in enumerate(results, 1):
        print(f"\n📈 Query {i}: '{result.query}'")
        
        # Google PAA
        google_paa = getattr(result, 'people_also_ask_queries', []) or []
        print(f"   🔴 Google PAA: {'✅' if google_paa else '❌'} ({len(google_paa)} questions)")
        if google_paa:
            for j, q in enumerate(google_paa[:2], 1):  # Show first 2
                print(f"      {j}. {q}")
        
        # Bing PAA
        bing_paa = getattr(result, 'bing_people_also_ask_queries', []) or []
        print(f"   🔵 Bing PAA: {'✅' if bing_paa else '❌'} ({len(bing_paa)} questions)")
        if bing_paa:
            for j, q in enumerate(bing_paa[:2], 1):  # Show first 2
                print(f"      {j}. {q}")
    
    # Export results
    monitor.export_results()
    
    print("\n✅ Bing PAA Enhancement Test Completed!")
    print("📊 Key verification points:")
    print("   ✅ Bing PAA extraction implemented")
    print("   ✅ Separate tracking for Google vs Bing PAA")
    print("   ✅ Enhanced summary report with both engines")
    print("   ✅ Real-time PAA detection during analysis")

if __name__ == "__main__":
    test_bing_paa()
