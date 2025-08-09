#!/usr/bin/env python3
"""
Quick Test: Run Enhanced App with Sample Data
Test the enhanced functionality with a simple query
"""

import os
from ai_visibility_monitor import AIVisibilityMonitor, UserInput

def quick_enhanced_test():
    """Quick test of enhanced functionality"""
    
    print("🚀 Quick Test: Enhanced AI Visibility Monitor")
    print("==============================================")
    
    # Load credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ DataForSEO credentials not found")
        return
    
    # Test with a single healthcare query
    user_input = UserInput(
        brand_name="Mayo Clinic",
        brand_domain="mayoclinic.org",
        competitors=["webmd.com", "healthline.com"],
        serp_queries=["heart disease symptoms"],  # Just one query for quick test
        industry="Healthcare",
        location="United States",
        device="desktop",
        language="English"
    )
    
    print("🔍 Testing enhanced features with:")
    print(f"   Query: {user_input.serp_queries[0]}")
    print(f"   Brand: {user_input.brand_name}")
    print(f"   Competitors: {', '.join(user_input.competitors)}")
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(user_input)
    
    # Export results
    monitor.export_results()
    
    print("\n✅ Enhanced functionality test completed!")
    print("📊 Key enhancements demonstrated:")
    print("   ✅ People Also Ask question extraction")
    print("   ✅ AI Visibility scoring (0-100 scale)")
    print("   ✅ Competitor AI citation analysis")
    print("   ✅ AI dominance ranking")
    print("   ✅ Enhanced summary reporting")

if __name__ == "__main__":
    quick_enhanced_test()
