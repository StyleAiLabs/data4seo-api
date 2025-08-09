#!/usr/bin/env python3
"""
Test the exact original business scenario that was showing false results
"""

from ai_visibility_monitor import AIVisibilityMonitor, UserInput
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('DATAFORSEO_LOGIN')
password = os.getenv('DATAFORSEO_PASSWORD')

print("🧪 Testing Original Business Scenario")
print("=" * 50)

monitor = AIVisibilityMonitor(login, password)

# Use the exact same input as the original business test
user_input = UserInput(
    brand_name="Mayo Clinic",
    brand_domain="mayoclinic.org",
    competitors=["webmd.com", "healthline.com", "clevelandclinic.org"],
    serp_queries=[
        "what causes diabetes",
        "heart disease symptoms", 
        "how to prevent cancer",
        "benefits of exercise",
        "healthy diet tips"
    ],
    industry="Healthcare", 
    location="United States",
    device="desktop"
)

print(f"\n🚀 Running analysis for all {len(user_input.serp_queries)} queries...")
print(f"📋 Queries: {user_input.serp_queries}")

# Run with timeout to avoid hanging
import signal

class TimeoutHandler:
    def __init__(self, timeout):
        self.timeout = timeout
        
    def __enter__(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self.timeout)
        return self
        
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
        
    def _timeout_handler(self, signum, frame):
        raise TimeoutError("Analysis timed out")

try:
    with TimeoutHandler(120):  # 2 minute timeout
        results = monitor.run_analysis(user_input)
        
    print(f"\n✅ Analysis completed!")
    print(f"\n📊 Detailed Results:")
    
    for i, result in enumerate(results, 1):
        if result.google_ai_overview_present:
            citation_status = "✅ CITED" if result.google_brand_cited else "❌ NOT CITED"
            print(f"   {i}. '{result.query}' - AI Overview: ✅ - Brand: {citation_status}")
        else:
            print(f"   {i}. '{result.query}' - AI Overview: ❌")

except TimeoutError:
    print(f"\n⏰ Analysis timed out after 2 minutes")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
