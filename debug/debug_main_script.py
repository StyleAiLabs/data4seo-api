#!/usr/bin/env python3
"""
Test the main script flow with heart disease symptoms
"""

from ai_visibility_monitor import AIVisibilityMonitor, UserInput
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('DATAFORSEO_LOGIN')
password = os.getenv('DATAFORSEO_PASSWORD')

print("🧪 Testing Main Script Flow")
print("=" * 40)

monitor = AIVisibilityMonitor(login, password)

# Test with single keyword
user_input = UserInput(
    brand_name="Mayo Clinic",
    brand_domain="mayoclinic.org",
    competitors=["webmd.com", "healthline.com"],
    serp_queries=["heart disease symptoms"],  # Just one query
    industry="Healthcare", 
    location="United States",
    device="desktop"
)

print(f"\n🔍 Testing single query: 'heart disease symptoms'")
print(f"🎯 Brand domain: {user_input.brand_domain}")

# Create analyzer (same as main script does)
from ai_visibility_monitor import AIVisibilityAnalyzer
analyzer = AIVisibilityAnalyzer(user_input.brand_domain, user_input.competitors)

# Get SERP data (same as main script)
serp_data = monitor.client.get_google_serp_advanced(
    keyword="heart disease symptoms",
    location=user_input.location,
    device=user_input.device,
    language="English"
)

# Analyze (same as main script)
google_analysis = analyzer.analyze_google_serp(serp_data)

print(f"\n📊 Analysis Results:")
print(f"   AI Overview Present: {google_analysis['ai_overview_present']}")
print(f"   Brand Cited: {google_analysis['brand_cited']} {'✅' if google_analysis['brand_cited'] else '❌'}")
print(f"   Total Citations: {len(google_analysis['ai_citations'])}")
print(f"   Citations: {google_analysis['ai_citations'][:5]}")

# Check if Mayo Clinic is in the citations
mayo_found = False
for citation in google_analysis['ai_citations']:
    if 'mayoclinic' in citation.lower():
        mayo_found = True
        print(f"   🎯 Mayo Clinic found as: {citation}")
        break

if not mayo_found:
    print(f"   ❌ Mayo Clinic NOT found in citations")

print(f"\n🔍 Brand domain being checked: '{user_input.brand_domain}'")
print(f"🔍 Analyzer brand domain: '{analyzer.brand_domain}'")
