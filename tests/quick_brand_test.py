#!/usr/bin/env python3
"""
Quick test of the fixed brand citation logic
"""

from ai_visibility_monitor import DataForSEOClient, AIVisibilityAnalyzer
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('DATAFORSEO_LOGIN')
password = os.getenv('DATAFORSEO_PASSWORD')

print("🧪 Quick Brand Citation Test")
print("=" * 40)

client = DataForSEOClient(login, password)
analyzer = AIVisibilityAnalyzer("mayoclinic.org", [])

# Test with the keyword we know has Mayo Clinic citation
serp_data = client.get_google_serp_advanced(
    keyword="heart disease symptoms",
    location="United States",
    device="desktop", 
    language="English"
)

analysis = analyzer.analyze_google_serp(serp_data)

print(f"📊 Results for 'heart disease symptoms':")
print(f"   AI Overview Present: {analysis['ai_overview_present']}")
print(f"   Brand Cited: {analysis['brand_cited']} {'✅' if analysis['brand_cited'] else '❌'}")
print(f"   Total Citations: {len(analysis['ai_citations'])}")

if 'www.mayoclinic.org' in analysis['ai_citations'] or 'mayoclinic.org' in analysis['ai_citations']:
    print(f"   🎯 Mayo Clinic found in citations!")
else:
    print(f"   ❌ Mayo Clinic NOT in citations")

print(f"\n🔗 First 5 citations: {analysis['ai_citations'][:5]}")
