#!/usr/bin/env python3
"""
Debug the actual main script output with minimal keywords
"""

from ai_visibility_monitor import AIVisibilityMonitor, UserInput
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('DATAFORSEO_LOGIN')
password = os.getenv('DATAFORSEO_PASSWORD')

print("🧪 Debugging Main Script with Minimal Input")
print("=" * 50)

monitor = AIVisibilityMonitor(login, password)

# Test with single keyword that we know should work
user_input = UserInput(
    brand_name="Mayo Clinic",
    brand_domain="mayoclinic.org",
    competitors=["webmd.com"],  # Just one competitor
    serp_queries=["heart disease symptoms"],  # Just one query
    industry="Healthcare", 
    location="United States",
    device="desktop"
)

print(f"\n🚀 Starting analysis...")
print(f"📊 Keywords to analyze: {user_input.serp_queries}")

# Run analysis but catch any issues
try:
    results = monitor.run_analysis(user_input)
    
    print(f"\n✅ Analysis completed!")
    print(f"📋 Results summary:")
    for result in results:
        print(f"   Query: '{result.query}'")
        print(f"   AI Overview: {result.google_ai_overview_present}")
        print(f"   Brand Cited: {result.google_brand_cited} {'✅' if result.google_brand_cited else '❌'}")
        print(f"   Citations: {len(result.google_ai_citations)}")
        print(f"   First 3 citations: {result.google_ai_citations[:3]}")
        print()
    
except Exception as e:
    print(f"❌ Error during analysis: {e}")
    import traceback
    traceback.print_exc()
