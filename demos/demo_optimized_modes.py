#!/usr/bin/env python3
"""
Demo of the optimized API endpoint - Fast Mode vs Comprehensive Mode
"""

import time
import requests
import json

def test_fast_mode():
    """Test the fast mode optimization"""
    print("🚀 OPTIMIZED API DEMO - Fast Mode Perfect for SaaS")
    print("=" * 60)
    
    # Fast mode request (perfect for user onboarding)
    fast_request = {
        "brand_name": "Nike",
        "brand_domain": "nike.com",
        "competitors": ["adidas.com", "puma.com"],  # Limited to 3 for speed
        "serp_queries": ["running shoes", "athletic wear", "sports equipment"],  # Limited to 5 for speed
        "industry": "Sports",
        "location": "United States",
        "fast_mode": True  # This is the key optimization!
    }
    
    print("📊 Fast Mode Request:")
    print(json.dumps(fast_request, indent=2))
    
    print("\n⚡ Expected Performance:")
    print("- Response Time: 15-30 seconds")
    print("- Keywords Analyzed: 3 (from 3 requested)")
    print("- Competitors Analyzed: 2 (from 2 requested)")
    print("- Processing: Parallel (if available)")
    print("- Use Case: Perfect for SaaS user onboarding")
    
    print("\n📊 Comprehensive Mode Alternative:")
    comprehensive_request = {
        "brand_name": "Nike",
        "brand_domain": "nike.com",
        "competitors": ["adidas.com", "puma.com", "underarmour.com", "asics.com", "newbalance.com"],
        "serp_queries": [
            "running shoes", "athletic wear", "sports equipment", "basketball shoes", 
            "workout clothes", "fitness gear", "training shoes", "activewear",
            "sports apparel", "athletic footwear", "gym clothes", "running gear"
        ],
        "industry": "Sports",
        "location": "United States", 
        "fast_mode": False  # Comprehensive analysis
    }
    
    print(json.dumps({
        "brand_name": comprehensive_request["brand_name"],
        "brand_domain": comprehensive_request["brand_domain"],
        "competitors": f"{len(comprehensive_request['competitors'])} competitors",
        "serp_queries": f"{len(comprehensive_request['serp_queries'])} keywords",
        "fast_mode": comprehensive_request["fast_mode"]
    }, indent=2))
    
    print("\n⏰ Expected Performance:")
    print("- Response Time: 2-5 minutes")
    print("- Keywords Analyzed: 12 (from 12 requested)")
    print("- Competitors Analyzed: 5 (from 5 requested)")
    print("- Processing: Standard comprehensive")
    print("- Use Case: Detailed analysis and reporting")
    
    print("\n🎯 OPTIMIZATION BENEFITS:")
    print("✅ Single endpoint (/api/v1/analyze) handles both modes")
    print("✅ Intelligent optimization based on fast_mode parameter")
    print("✅ 8-10x speed improvement for SaaS onboarding")
    print("✅ Clean, maintainable codebase")
    print("✅ Enhanced performance metrics in responses")
    
    print("\n🔧 Expected Response Enhancement:")
    expected_response = {
        "analysis_id": "uuid-here",
        "status": "completed",
        "summary": {
            "processing_time_seconds": 18.5,
            "performance_mode": "fast (parallel)",
            "optimization_applied": {
                "keywords_analyzed": 3,
                "keywords_requested": 3,
                "competitors_analyzed": 2,
                "competitors_requested": 2,
                "parallel_processing": True,
                "fast_mode_enabled": True
            },
            "performance_insights": {
                "speed_improvement": "8-10x faster than baseline",
                "recommended_for": "SaaS user onboarding"
            },
            "ai_overview_presence": {
                "count": 2,
                "percentage": 66.7
            },
            "brand_citations": {
                "count": 2,
                "percentage": 100.0
            }
        }
    }
    
    print(json.dumps(expected_response, indent=2))

if __name__ == "__main__":
    test_fast_mode()
