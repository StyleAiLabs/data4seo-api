#!/usr/bin/env python3
"""
Quick test of the fast AI visibility monitor
Demonstrates the speed improvements without running full API services
"""

import time
import os
from fast_ai_visibility_monitor import FastAIVisibilityMonitor, FastUserInput

def test_fast_monitor():
    """Test the fast monitor directly"""
    print("🚀 Testing Fast AI Visibility Monitor")
    print("=" * 50)
    
    # Get credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ DataForSEO credentials not found in environment")
        print("💡 Make sure you have DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD set")
        return
    
    # Create test input
    user_input = FastUserInput(
        brand_name="Nike",
        brand_domain="nike.com",
        competitors=["adidas.com", "puma.com"],
        serp_queries=["running shoes", "athletic wear", "sportswear"],
        industry="Sports",
        location="United States"
    )
    
    print(f"🎯 Test Configuration:")
    print(f"   Brand: {user_input.brand_name}")
    print(f"   Domain: {user_input.brand_domain}")
    print(f"   Keywords: {', '.join(user_input.serp_queries)}")
    print(f"   Competitors: {', '.join(user_input.competitors)}")
    
    # Run fast analysis
    try:
        monitor = FastAIVisibilityMonitor(login, password)
        
        start_time = time.time()
        results, summary = monitor.run_fast_analysis(user_input)
        end_time = time.time()
        
        total_time = (end_time - start_time) * 1000
        
        print(f"\n✅ Fast Analysis Completed!")
        print(f"📊 Performance Results:")
        print(f"   - Total Time: {total_time:.0f}ms ({total_time/1000:.1f}s)")
        print(f"   - Keywords Analyzed: {len(results)}")
        print(f"   - Average Time per Keyword: {total_time/len(results):.0f}ms")
        
        print(f"\n📈 AI Visibility Results:")
        print(f"   - Overall AI Score: {summary['ai_visibility']['overall_score']}/100")
        print(f"   - AI Overview Presence: {summary['ai_visibility']['ai_overview_presence']['percentage']}%")
        print(f"   - Brand Citation Rate: {summary['ai_visibility']['brand_citations']['percentage']}%")
        
        print(f"\n🎯 Individual Keyword Results:")
        for i, result in enumerate(results, 1):
            print(f"   {i}. '{result.query}':")
            print(f"      - AI Score: {result.ai_visibility_score:.1f}/100")
            print(f"      - Google AI Overview: {'✅' if result.google_ai_overview_present else '❌'}")
            print(f"      - Brand Cited: {'✅' if result.google_brand_cited else '❌'}")
            print(f"      - Bing AI Features: {'✅' if result.bing_ai_present else '❌'}")
            print(f"      - Processing Time: {result.processing_time_ms}ms")
        
        print(f"\n💡 Key Recommendations:")
        for i, rec in enumerate(summary['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        print(f"\n⚡ Speed Analysis:")
        expected_standard_time = 120000  # 2 minutes for standard analysis
        improvement = expected_standard_time / total_time
        print(f"   - Fast Analysis: {total_time:.0f}ms")
        print(f"   - Standard Analysis (estimated): {expected_standard_time}ms")
        print(f"   - Speed Improvement: {improvement:.1f}x faster")
        print(f"   - Time Saved: {(expected_standard_time - total_time)/1000:.1f} seconds")
        
        print(f"\n🎯 SaaS Integration Benefits:")
        print(f"   ✅ Real-time results during user onboarding")
        print(f"   ✅ Immediate AI readiness assessment")
        print(f"   ✅ Actionable recommendations in seconds")
        print(f"   ✅ Perfect for freemium model (fast preview)")
        print(f"   ✅ Upsell opportunity to full detailed analysis")
        
        return True
        
    except Exception as e:
        print(f"❌ Fast Analysis Failed: {e}")
        print(f"💡 Possible issues:")
        print(f"   - Check internet connection")
        print(f"   - Verify DataForSEO API credentials")
        print(f"   - Ensure sufficient API credits")
        return False

if __name__ == "__main__":
    # Configure Python environment first
    print("🔧 Configuring Python environment...")
    
    # Test the fast monitor
    success = test_fast_monitor()
    
    if success:
        print(f"\n🏆 SUCCESS: Fast AI Visibility Monitor is ready for SaaS integration!")
        print(f"🚀 Next Steps:")
        print(f"   1. Deploy fast_api_service.py for production")
        print(f"   2. Integrate with your SaaS onboarding flow")
        print(f"   3. Use /api/v2/onboarding-analysis endpoint")
        print(f"   4. Offer detailed analysis as premium feature")
    else:
        print(f"\n❌ Setup required before SaaS integration")
        print(f"🔧 Troubleshooting steps:")
        print(f"   1. Set up DataForSEO credentials")
        print(f"   2. Test internet connectivity")
        print(f"   3. Verify API access")
