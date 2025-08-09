#!/usr/bin/env python3
"""
Analyze Existing Results for Enhanced Insights
Demonstrate insights on the previous heart disease symptoms data
"""

import json
from typing import Dict, List

def analyze_existing_results():
    """Analyze the existing results file for enhanced insights"""
    
    print("🔍 Analyzing Existing Results: heart disease symptoms")
    print("===================================================")
    
    # Read the existing results file
    try:
        with open('/workspaces/data4seo-api/results/ai_visibility_results_20250809_111939.json', 'r') as f:
            results = json.load(f)
    except FileNotFoundError:
        print("❌ Results file not found")
        return
    
    # Find the heart disease symptoms result
    heart_disease_result = None
    for result in results:
        if result['query'] == 'heart disease symptoms':
            heart_disease_result = result
            break
    
    if not heart_disease_result:
        print("❌ Heart disease symptoms result not found")
        return
    
    print(f"📊 Query: {heart_disease_result['query']}")
    print(f"📅 Timestamp: {heart_disease_result['timestamp']}")
    print(f"📍 Location: {heart_disease_result['location']}")
    
    # AI Overview Analysis
    print(f"\n🔴 GOOGLE AI OVERVIEW ANALYSIS")
    print(f"Present: {'✅ Yes' if heart_disease_result['google_ai_overview_present'] else '❌ No'}")
    print(f"Brand Cited: {'✅ Yes (Mayo Clinic found!)' if heart_disease_result['google_brand_cited'] else '❌ No'}")
    
    # Citations Analysis
    citations = heart_disease_result.get('google_ai_citations', [])
    if not isinstance(citations, list):
        citations = []
    
    print(f"\n📚 AI OVERVIEW CITATIONS ({len(citations)} total):")
    
    # Group citations by domain type
    healthcare_domains = []
    educational_domains = []
    government_domains = []
    other_domains = []
    
    for citation in citations:
        citation_clean = citation.lower().replace('www.', '')
        if any(keyword in citation_clean for keyword in ['clinic', 'hospital', 'health', 'medical', 'heart']):
            healthcare_domains.append(citation)
        elif any(keyword in citation_clean for keyword in ['harvard', 'edu', '.ac.']):
            educational_domains.append(citation)
        elif any(keyword in citation_clean for keyword in ['gov', 'nhs', 'cdc']):
            government_domains.append(citation)
        else:
            other_domains.append(citation)
    
    if healthcare_domains:
        print(f"  🏥 Healthcare Institutions ({len(healthcare_domains)}):")
        for domain in healthcare_domains[:5]:  # Show top 5
            indicator = "👑" if "mayoclinic" in domain.lower() else "🔸"
            print(f"    {indicator} {domain}")
    
    if educational_domains:
        print(f"  🎓 Educational Institutions ({len(educational_domains)}):")
        for domain in educational_domains[:3]:
            print(f"    🔸 {domain}")
    
    if government_domains:
        print(f"  🏛️ Government/Health Authorities ({len(government_domains)}):")
        for domain in government_domains[:3]:
            print(f"    🔸 {domain}")
    
    # Competitor Analysis
    competitors = heart_disease_result.get('google_competitor_citations', {})
    print(f"\n🏆 COMPETITOR ANALYSIS")
    if competitors:
        print("Competitors found in AI Overview:")
        for comp, comp_citations in competitors.items():
            print(f"  🔸 {comp}: {comp_citations} citation(s)")
    else:
        print("  ℹ️  No specified competitors found in AI Overview")
    
    # Calculate Mayo Clinic's authority score
    mayo_cited = heart_disease_result['google_brand_cited']
    total_citations = len(citations)
    mayo_authority = 100 if mayo_cited else 0
    
    print(f"\n📊 AUTHORITY ANALYSIS")
    print(f"Mayo Clinic Authority Score: {mayo_authority}/100")
    print(f"Citation Diversity: {len(set(citations))} unique domains")
    print(f"Healthcare Domain Dominance: {len(healthcare_domains)}/{total_citations} ({len(healthcare_domains)/total_citations*100:.1f}%)")
    
    # SERP Features
    print(f"\n📈 SERP FEATURES PRESENCE")
    features = {
        "Knowledge Graph": heart_disease_result.get('knowledge_graph_present', False),
        "People Also Ask": heart_disease_result.get('people_also_ask_present', False),
        "Featured Snippet": heart_disease_result.get('featured_snippet_present', False)
    }
    
    for feature, present in features.items():
        print(f"  {feature}: {'✅' if present else '❌'}")
    
    print(f"\n💡 KEY INSIGHTS")
    print("="*30)
    
    if mayo_cited:
        print("✅ STRONG POSITION: Mayo Clinic is cited in AI Overview")
        print("   - Brand successfully appears in authoritative AI-generated content")
        print("   - High trust signal from Google's AI systems")
    
    healthcare_ratio = len(healthcare_domains) / total_citations if total_citations > 0 else 0
    if healthcare_ratio > 0.7:
        print("✅ DOMAIN AUTHORITY: Healthcare institutions dominate citations")
        print("   - Query attracts highly relevant, authoritative sources")
        print("   - Mayo Clinic competes in premium healthcare space")
    
    if len(set(citations)) == len(citations):
        print("✅ CITATION QUALITY: All citations from unique domains")
        print("   - Diverse, high-quality source portfolio")
        print("   - Reduced risk of AI Overview bias")
    
    if heart_disease_result.get('people_also_ask_present'):
        print("✅ CONTENT OPPORTUNITY: People Also Ask present")
        print("   - High user interest and query expansion potential")
        print("   - Opportunity for content optimization")
    
    print(f"\n🎯 RECOMMENDATIONS")
    print("="*20)
    print("1. 🎉 MAINTAIN EXCELLENCE: Continue high-quality heart disease content")
    print("2. 📝 EXPAND COVERAGE: Target related PAA questions for content")
    print("3. 👀 MONITOR COMPETITORS: Track competitor citation growth")
    print("4. 🔗 BUILD AUTHORITY: Strengthen citations and backlink profile")

if __name__ == "__main__":
    analyze_existing_results()
