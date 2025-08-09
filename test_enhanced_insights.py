#!/usr/bin/env python3
"""
Test Enhanced AI Visibility Insights
Test People Also Ask extraction and competitor AI visibility scoring
"""

import os
from ai_visibility_monitor import AIVisibilityMonitor, UserInput

def test_enhanced_insights():
    """Test the enhanced insights functionality"""
    
    print("🧪 Testing Enhanced AI Visibility Insights")
    print("==========================================")
    
    # Load credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ DataForSEO credentials not found")
        print("Set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD environment variables")
        return
    
    # Test with healthcare scenario (known to have AI Overviews and PAA)
    user_input = UserInput(
        brand_name="Mayo Clinic",
        brand_domain="mayoclinic.org",
        competitors=["mountsinai.org", "health.harvard.edu", "clevelandclinic.org"],
        serp_queries=["heart disease symptoms", "diabetes treatment", "healthy diet tips"],
        industry="Healthcare",
        location="United States",
        device="desktop",
        language="English"
    )
    
    print(f"🏥 Testing Healthcare Scenario:")
    print(f"Brand: {user_input.brand_name}")
    print(f"Competitors: {', '.join(user_input.competitors)}")
    print(f"Keywords: {', '.join(user_input.serp_queries)}")
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(user_input)
    
    print("\n🔍 Detailed Results Analysis:")
    print("==============================")
    
    for i, result in enumerate(results, 1):
        print(f"\n📈 Result {i}: '{result.query}'")
        print(f"   AI Overview: {'✅' if result.google_ai_overview_present else '❌'}")
        print(f"   Brand Cited: {'✅' if result.google_brand_cited else '❌'}")
        print(f"   AI Score: {result.ai_visibility_score:.1f}/100")
        print(f"   Dominance Rank: #{result.ai_dominance_rank}")
        
        if hasattr(result, 'people_also_ask_queries') and result.people_also_ask_queries:
            print(f"   PAA Questions ({len(result.people_also_ask_queries)}):")
            for j, question in enumerate(result.people_also_ask_queries[:3], 1):  # Show first 3
                print(f"     {j}. {question}")
            if len(result.people_also_ask_queries) > 3:
                print(f"     ... and {len(result.people_also_ask_queries) - 3} more")
        
        if hasattr(result, 'competitor_ai_scores') and result.competitor_ai_scores:
            print(f"   Competitor Scores:")
            for comp, score in result.competitor_ai_scores.items():
                print(f"     {comp}: {score:.1f}/100")
    
    # Export enhanced results
    monitor.export_results()
    
    print("\n✅ Enhanced insights testing completed!")
    print("📊 Check the summary report above for:")
    print("   - People Also Ask insights")
    print("   - AI Visibility scores")
    print("   - Competitor comparisons")
    print("   - AI dominance rankings")

if __name__ == "__main__":
    test_enhanced_insights()
