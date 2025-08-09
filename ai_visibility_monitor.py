#!/usr/bin/env python3
"""
RankAled Phase 1: AI Search Visibility Monitor
Integrates DataForSEO APIs to track brand visibility across AI-powered search results
"""

import json
import requests
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import os

# Load environment variables from .env file if it exists
def load_env():
    """Load environment variables from .env file"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env()

@dataclass
class UserInput:
    """User journey input parameters"""
    brand_name: str
    brand_domain: str
    competitors: List[str]  # competitor domains
    serp_queries: List[str]  # keywords to monitor
    industry: str
    location: str  # "London,England,United Kingdom"
    device: str = "desktop"  # desktop, mobile, tablet
    language: str = "English"

@dataclass
class AIVisibilityResult:
    """Aggregated AI visibility metrics"""
    query: str
    location: str
    device: str
    timestamp: str
    
    # Google AI Overview
    google_ai_overview_present: bool = False
    google_ai_citations: List[str] = None
    google_brand_cited: bool = False
    google_competitor_citations: Dict[str, int] = None
    
    # Bing AI Features
    bing_ai_features: List[str] = None
    bing_brand_visibility: bool = False
    
    # SERP Features
    featured_snippet_present: bool = False
    knowledge_graph_present: bool = False
    people_also_ask_present: bool = False

class DataForSEOClient:
    """DataForSEO API client for AI visibility monitoring"""
    
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.base_url = "https://api.dataforseo.com/v3"
        self.session = requests.Session()
        self.session.auth = (login, password)
        self.session.headers.update({'Content-Type': 'application/json'})
    
    def get_location_code(self, location_name: str) -> int:
        """Convert location name to DataForSEO location code"""
        location_mapping = {
            "United States": 2840,
            "New Zealand": 2554,
            "United Kingdom": 2826,
            "Australia": 2036,
            "Canada": 2124,
            "London,England,United Kingdom": 2826,
            "Auckland,New Zealand": 2554,
            "Sydney,Australia": 2036,
            "Toronto,Canada": 2124,
            "New York,United States": 2840,
            "Los Angeles,United States": 2840,
            "default": 2840  # Default to US
        }
        
        # Try exact match first
        if location_name in location_mapping:
            return location_mapping[location_name]
        
        # Try partial matching for common patterns
        location_lower = location_name.lower()
        if "new zealand" in location_lower:
            return 2554
        elif "united kingdom" in location_lower or "uk" in location_lower:
            return 2826
        elif "australia" in location_lower:
            return 2036
        elif "canada" in location_lower:
            return 2124
        elif "united states" in location_lower or "usa" in location_lower:
            return 2840
        
        return location_mapping["default"]
    
    def get_language_code(self, language_name: str) -> str:
        """Convert language name to DataForSEO language code"""
        language_mapping = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "default": "en"  # Default to English
        }
        return language_mapping.get(language_name, language_mapping["default"])
    
    def get_available_locations(self) -> Dict[str, Any]:
        """Get available locations from DataForSEO"""
        url = f"{self.base_url}/serp/google/locations"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching locations: {e}")
            return {}
    
    def get_available_languages(self) -> Dict[str, Any]:
        """Get available languages from DataForSEO"""
        url = f"{self.base_url}/serp/google/languages"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching languages: {e}")
            return {}
    
    def check_task_status(self, task_id: str, service: str = "google") -> Dict[str, Any]:
        """Check the status of a posted task"""
        if service == "google":
            url = f"{self.base_url}/serp/google/organic/tasks_ready"
        else:  # bing
            url = f"{self.base_url}/serp/bing/organic/tasks_ready"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data.get('tasks'):
                for task in data['tasks']:
                    if task.get('id') == task_id:
                        return {'ready': True, 'task': task}
            
            return {'ready': False, 'task': None}
        except Exception as e:
            print(f"Error checking task status for {task_id}: {e}")
            return {'ready': False, 'task': None}
    
    def wait_for_task_completion(self, task_id: str, service: str = "google", max_wait: int = 30) -> bool:
        """Wait for task completion with timeout"""
        wait_time = 0
        
        while wait_time < max_wait:
            status = self.check_task_status(task_id, service)
            if status['ready']:
                return True
            
            time.sleep(2)
            wait_time += 2
            print(f"    ⏳ Waiting for task {task_id}... ({wait_time}s)")
        
        print(f"    ⚠️  Timeout waiting for task {task_id}")
        return False
    
    def discover_brand_keywords(self, domain: str, location: str = "United States", language: str = "English", limit: int = 100) -> List[str]:
        """Get keywords the brand domain ranks for using DataForSEO Labs"""
        url = f"{self.base_url}/dataforseo_labs/google/keywords_for_site/live"
        
        location_code = self.get_location_code(location)
        language_code = self.get_language_code(language)
        
        payload = [{
            "target": domain,
            "location_code": location_code,
            "language_code": language_code,
            "limit": limit,
            "filters": [
                ["keyword_info.search_volume", ">", 100]
            ]
        }]
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            
            data = response.json()
            keywords = []
            
            if data.get('tasks') and data['tasks'][0].get('result'):
                for item in data['tasks'][0]['result']:
                    # Handle the correct response structure for keywords_for_site
                    if 'keyword_info' in item and 'keyword' in item['keyword_info']:
                        keyword = item['keyword_info']['keyword']
                        keywords.append(keyword)
                    elif 'keyword' in item:
                        keyword = item['keyword']
                        keywords.append(keyword)
            
            return keywords[:50]  # Return top 50 keywords
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 402:
                print(f"⚠️  Insufficient credits for keyword discovery - using provided keywords only")
            else:
                print(f"Error discovering keywords for {domain}: HTTP {e.response.status_code}")
            return []
        except Exception as e:
            print(f"Error discovering keywords for {domain}: {e}")
            return []
    
    def get_google_serp_advanced(self, keyword: str, location: str, device: str, language: str) -> Dict[str, Any]:
        """Get Google SERP with AI Overview and all SERP features using live endpoint"""
        url = f"{self.base_url}/serp/google/organic/live/advanced"
        
        location_code = self.get_location_code(location)
        language_code = self.get_language_code(language)
        
        payload = [{
            "keyword": keyword,
            "location_code": location_code,
            "language_code": language_code,
            "device": device,
            "os": "windows" if device == "desktop" else "android"
        }]
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 402:
                print(f"⚠️  Insufficient credits for Google SERP - '{keyword}'")
            elif e.response.status_code == 404:
                print(f"⚠️  Google SERP endpoint not available for location '{location}'")
            else:
                print(f"Error fetching Google SERP for '{keyword}': HTTP {e.response.status_code}")
            return {}
        except Exception as e:
            print(f"Error fetching Google SERP for '{keyword}': {e}")
            return {}
    
    def get_bing_serp_advanced(self, keyword: str, location: str, device: str, language: str) -> Dict[str, Any]:
        """Get Bing SERP with AI features using live endpoint"""
        url = f"{self.base_url}/serp/bing/organic/live/advanced"
        
        location_code = self.get_location_code(location)
        language_code = self.get_language_code(language)
        
        payload = [{
            "keyword": keyword,
            "location_code": location_code,
            "language_code": language_code,
            "device": device
        }]
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 402:
                print(f"⚠️  Insufficient credits for Bing SERP - '{keyword}'")
            elif e.response.status_code == 404:
                print(f"⚠️  Bing SERP endpoint not available for location '{location}'")
            else:
                print(f"Error fetching Bing SERP for '{keyword}': HTTP {e.response.status_code}")
            return {}
        except Exception as e:
            print(f"Error fetching Bing SERP for '{keyword}': {e}")
            return {}
    
    def get_knowledge_graph(self, brand_name: str, location: str, language: str) -> Dict[str, Any]:
        """Get Google Knowledge Graph for brand entity using live endpoint"""
        url = f"{self.base_url}/serp/google/organic/live/advanced"
        
        location_code = self.get_location_code(location)
        language_code = self.get_language_code(language)
        
        payload = [{
            "keyword": brand_name,
            "location_code": location_code,
            "language_code": language_code,
            "device": "desktop"
        }]
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            
            # Extract Knowledge Graph from organic results
            if data.get('tasks') and data['tasks'][0].get('result'):
                items = data['tasks'][0]['result'][0].get('items', [])
                for item in items:
                    if item.get('type') == 'knowledge_graph':
                        return {'knowledge_graph_found': True, 'data': item}
            
            return {'knowledge_graph_found': False, 'data': None}
            
        except Exception as e:
            print(f"Error fetching Knowledge Graph for '{brand_name}': {e}")
            return {'knowledge_graph_found': False, 'data': None}

class AIVisibilityAnalyzer:
    """Analyzes SERP data for AI visibility metrics"""
    
    def __init__(self, brand_domain: str, competitor_domains: List[str]):
        self.brand_domain = brand_domain
        self.competitor_domains = competitor_domains
    
    def extract_domain_from_url(self, url: str) -> str:
        """Extract domain from URL"""
        if not url:
            return ""
        try:
            from urllib.parse import urlparse
            return urlparse(url).netloc.lower().replace('www.', '')
        except:
            return ""
    
    def analyze_google_serp(self, serp_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze Google SERP for AI Overview and SERP features"""
        analysis = {
            'ai_overview_present': False,
            'ai_citations': [],
            'brand_cited': False,
            'competitor_citations': {},
            'featured_snippet_present': False,
            'knowledge_graph_present': False,
            'people_also_ask_present': False
        }
        
        if not serp_data.get('tasks') or not serp_data['tasks'][0].get('result'):
            return analysis
        
        items = serp_data['tasks'][0]['result'][0].get('items', [])
        
        for item in items:
            item_type = item.get('type', '')
            
            # AI Overview analysis
            if item_type == 'ai_overview':
                analysis['ai_overview_present'] = True
                
                # Extract citations from AI Overview using the correct structure
                citations_found = False
                
                # Try 'references' field first (newer structure)
                if 'references' in item and item['references']:
                    for ref in item['references']:
                        url = ref.get('url', '')
                        domain = ref.get('domain') or self.extract_domain_from_url(url)
                        if domain:
                            citations_found = True
                            analysis['ai_citations'].append(domain)
                            
                            # Check brand citation (clean both domains for comparison)
                            domain_clean = domain.lower().replace('www.', '')
                            brand_clean = self.brand_domain.lower().replace('www.', '')
                            if domain_clean == brand_clean:
                                analysis['brand_cited'] = True
                            
                            # Count competitor citations
                            for comp_domain in self.competitor_domains:
                                comp_clean = comp_domain.lower().replace('www.', '')
                                domain_clean_for_comp = domain.lower().replace('www.', '')
                                if domain_clean_for_comp == comp_clean:
                                    analysis['competitor_citations'][comp_domain] = analysis['competitor_citations'].get(comp_domain, 0) + 1
                
                # Try 'items' field as fallback
                if not citations_found and 'items' in item and item['items']:
                    for sub_item in item['items']:
                        url = sub_item.get('url', '')
                        domain = sub_item.get('domain') or self.extract_domain_from_url(url)
                        if domain:
                            citations_found = True
                            analysis['ai_citations'].append(domain)
                            
                            # Check brand citation (clean both domains for comparison)
                            domain_clean = domain.lower().replace('www.', '')
                            brand_clean = self.brand_domain.lower().replace('www.', '')
                            if domain_clean == brand_clean:
                                analysis['brand_cited'] = True
                            
                            # Count competitor citations
                            for comp_domain in self.competitor_domains:
                                comp_clean = comp_domain.lower().replace('www.', '')
                                domain_clean_for_comp = domain.lower().replace('www.', '')
                                if domain_clean_for_comp == comp_clean:
                                    analysis['competitor_citations'][comp_domain] = analysis['competitor_citations'].get(comp_domain, 0) + 1
                
                # Legacy fallback to 'links' field
                if not citations_found and 'links' in item and item['links']:
                    for link in item['links']:
                        url = link.get('url', '')
                        domain = self.extract_domain_from_url(url)
                        if domain:
                            analysis['ai_citations'].append(domain)
                            
                            # Check brand citation (clean both domains for comparison)
                            domain_clean = domain.lower().replace('www.', '')
                            brand_clean = self.brand_domain.lower().replace('www.', '')
                            if domain_clean == brand_clean:
                                analysis['brand_cited'] = True
                            
                            # Count competitor citations
                            for comp_domain in self.competitor_domains:
                                comp_clean = comp_domain.lower().replace('www.', '')
                                domain_clean_for_comp = domain.lower().replace('www.', '')
                                if domain_clean_for_comp == comp_clean:
                                    analysis['competitor_citations'][comp_domain] = analysis['competitor_citations'].get(comp_domain, 0) + 1
                                if domain == comp_clean:
                                    analysis['competitor_citations'][comp_domain] = analysis['competitor_citations'].get(comp_domain, 0) + 1
            
            # Other SERP features
            elif item_type == 'featured_snippet':
                analysis['featured_snippet_present'] = True
            elif item_type == 'knowledge_graph':
                analysis['knowledge_graph_present'] = True
            elif item_type == 'people_also_ask':
                analysis['people_also_ask_present'] = True
        
        return analysis
    
    def analyze_bing_serp(self, serp_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze Bing SERP for AI features"""
        analysis = {
            'ai_features': [],
            'brand_visibility': False
        }
        
        if not serp_data.get('tasks') or not serp_data['tasks'][0].get('result'):
            return analysis
        
        items = serp_data['tasks'][0]['result'][0].get('items', [])
        
        for item in items:
            item_type = item.get('type', '')
            
            # Bing AI features
            if item_type in ['answer_box', 'instant_answer', 'knowledge_graph']:
                analysis['ai_features'].append(item_type)
                
                # Check if brand is mentioned (clean both domains for comparison)
                url = item.get('url', '')
                domain = self.extract_domain_from_url(url)
                if domain:
                    domain_clean = domain.lower().replace('www.', '')
                    brand_clean = self.brand_domain.lower().replace('www.', '')
                    if domain_clean == brand_clean:
                        analysis['brand_visibility'] = True
        
        return analysis

class AIVisibilityMonitor:
    """Main class for AI visibility monitoring user journey"""
    
    def __init__(self, dataforseo_login: str, dataforseo_password: str):
        self.client = DataForSEOClient(dataforseo_login, dataforseo_password)
        self.results = []
    
    def run_analysis(self, user_input: UserInput) -> List[AIVisibilityResult]:
        """Main user journey: analyze AI visibility for brand"""
        print(f"\n🚀 Starting AI Visibility Analysis for {user_input.brand_name}")
        print(f"📍 Location: {user_input.location}")
        print(f"📱 Device: {user_input.device}")
        print(f"🏭 Industry: {user_input.industry}")
        
        analyzer = AIVisibilityAnalyzer(user_input.brand_domain, user_input.competitors)
        
        # Step 1: Discover additional brand keywords
        print(f"\n🔍 Discovering keywords for {user_input.brand_domain}...")
        discovered_keywords = self.client.discover_brand_keywords(
            user_input.brand_domain, 
            user_input.location, 
            user_input.language
        )
        all_keywords = list(set(user_input.serp_queries + discovered_keywords))
        print(f"📊 Total keywords to analyze: {len(all_keywords)}")
        
        # Step 2: Get Knowledge Graph for brand entity
        print(f"\n📚 Checking for Knowledge Graph for {user_input.brand_name}...")
        kg_data = self.client.get_knowledge_graph(
            user_input.brand_name, 
            user_input.location, 
            user_input.language
        )
        
        if kg_data.get('knowledge_graph_found'):
            print(f"✅ Knowledge Graph found for {user_input.brand_name}")
        else:
            print(f"ℹ️  No Knowledge Graph found for {user_input.brand_name}")
        
        # Step 3: Analyze each keyword
        for i, keyword in enumerate(all_keywords[:20], 1):  # Limit to 20 keywords for demo
            print(f"\n📈 Analyzing keyword {i}/20: '{keyword}'")
            
            result = AIVisibilityResult(
                query=keyword,
                location=user_input.location,
                device=user_input.device,
                timestamp=datetime.now().isoformat(),
                google_competitor_citations={},
                google_ai_citations=[],
                bing_ai_features=[]
            )
            
            # Google SERP Analysis
            print(f"  🔴 Fetching Google SERP...")
            google_data = self.client.get_google_serp_advanced(
                keyword, user_input.location, user_input.device, user_input.language
            )
            
            if google_data:
                google_analysis = analyzer.analyze_google_serp(google_data)
                result.google_ai_overview_present = google_analysis['ai_overview_present']
                result.google_ai_citations = google_analysis['ai_citations']
                result.google_brand_cited = google_analysis['brand_cited']
                result.google_competitor_citations = google_analysis['competitor_citations']
                result.featured_snippet_present = google_analysis['featured_snippet_present']
                result.knowledge_graph_present = google_analysis['knowledge_graph_present']
                result.people_also_ask_present = google_analysis['people_also_ask_present']
                
                if google_analysis['ai_overview_present']:
                    print(f"    ✅ AI Overview found! Brand cited: {google_analysis['brand_cited']}")
                else:
                    print(f"    ❌ No AI Overview")
            
            # Bing SERP Analysis
            print(f"  🔵 Fetching Bing SERP...")
            bing_data = self.client.get_bing_serp_advanced(
                keyword, user_input.location, user_input.device, user_input.language
            )
            
            if bing_data:
                bing_analysis = analyzer.analyze_bing_serp(bing_data)
                result.bing_ai_features = bing_analysis['ai_features']
                result.bing_brand_visibility = bing_analysis['brand_visibility']
                
                if bing_analysis['ai_features']:
                    print(f"    ✅ Bing AI features: {', '.join(bing_analysis['ai_features'])}")
                else:
                    print(f"    ❌ No Bing AI features")
            
            self.results.append(result)
            
            # Rate limiting
            time.sleep(1)
        
        # Step 4: Generate summary report
        self.generate_summary_report(user_input)
        
        return self.results
    
    def generate_summary_report(self, user_input: UserInput):
        """Generate summary report of AI visibility"""
        print(f"\n\n📊 AI VISIBILITY SUMMARY REPORT")
        print(f"{'='*50}")
        print(f"Brand: {user_input.brand_name}")
        print(f"Domain: {user_input.brand_domain}")
        print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Keywords Analyzed: {len(self.results)}")
        
        if not self.results:
            print("❌ No results to analyze")
            return
        
        # Google AI Overview metrics
        ai_overview_count = sum(1 for r in self.results if r.google_ai_overview_present)
        brand_citations = sum(1 for r in self.results if r.google_brand_cited)
        
        print(f"\n🔴 GOOGLE AI OVERVIEW METRICS")
        print(f"AI Overview Presence: {ai_overview_count}/{len(self.results)} ({ai_overview_count/len(self.results)*100:.1f}%)")
        print(f"Brand Citations: {brand_citations}/{ai_overview_count if ai_overview_count > 0 else 1} ({brand_citations/(ai_overview_count if ai_overview_count > 0 else 1)*100:.1f}%)")
        
        # Competitor analysis
        all_competitor_citations = {}
        for result in self.results:
            for comp, count in result.google_competitor_citations.items():
                all_competitor_citations[comp] = all_competitor_citations.get(comp, 0) + count
        
        if all_competitor_citations:
            print(f"\n🏆 COMPETITOR AI CITATIONS")
            for comp, citations in sorted(all_competitor_citations.items(), key=lambda x: x[1], reverse=True):
                print(f"  {comp}: {citations} citations")
        
        # Bing AI features
        bing_features_count = sum(1 for r in self.results if r.bing_ai_features)
        bing_brand_visibility = sum(1 for r in self.results if r.bing_brand_visibility)
        
        print(f"\n🔵 BING AI FEATURES")
        print(f"AI Features Present: {bing_features_count}/{len(self.results)} ({bing_features_count/len(self.results)*100:.1f}%)")
        print(f"Brand Visibility: {bing_brand_visibility}/{bing_features_count if bing_features_count > 0 else 1} ({bing_brand_visibility/(bing_features_count if bing_features_count > 0 else 1)*100:.1f}%)")
        
        # SERP Features
        featured_snippets = sum(1 for r in self.results if r.featured_snippet_present)
        knowledge_graphs = sum(1 for r in self.results if r.knowledge_graph_present)
        people_also_ask = sum(1 for r in self.results if r.people_also_ask_present)
        
        print(f"\n📈 OTHER SERP FEATURES")
        print(f"Featured Snippets: {featured_snippets}/{len(self.results)} ({featured_snippets/len(self.results)*100:.1f}%)")
        print(f"Knowledge Graph: {knowledge_graphs}/{len(self.results)} ({knowledge_graphs/len(self.results)*100:.1f}%)")
        print(f"People Also Ask: {people_also_ask}/{len(self.results)} ({people_also_ask/len(self.results)*100:.1f}%)")
    
    def export_results(self, filename: str = None):
        """Export results to JSON"""
        if not filename:
            filename = f"results/ai_visibility_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Ensure results directory exists
        import os
        os.makedirs('results', exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump([asdict(result) for result in self.results], f, indent=2)
        
        print(f"\n💾 Results exported to: {filename}")

def main():
    """Interactive user journey"""
    print("🤖 RankAled Phase 1: AI Search Visibility Monitor")
    print("="*50)
    
    # Get DataForSEO credentials
    login = os.getenv('DATAFORSEO_LOGIN') or input("DataForSEO Login: ")
    password = os.getenv('DATAFORSEO_PASSWORD') or input("DataForSEO Password: ")
    
    # Collect user input
    print("\n📝 Enter your monitoring parameters:")
    
    brand_name = input("Brand Name: ")
    brand_domain = input("Brand Domain (e.g., example.com): ")
    
    competitors_input = input("Competitor Domains (comma-separated): ")
    competitors = [comp.strip() for comp in competitors_input.split(',') if comp.strip()]
    
    queries_input = input("SERP Queries to Monitor (comma-separated): ")
    serp_queries = [q.strip() for q in queries_input.split(',') if q.strip()]
    
    industry = input("Industry: ")
    location = input("Location (e.g., 'London,England,United Kingdom'): ")
    device = input("Device (desktop/mobile/tablet) [desktop]: ") or "desktop"
    
    user_input = UserInput(
        brand_name=brand_name,
        brand_domain=brand_domain,
        competitors=competitors,
        serp_queries=serp_queries,
        industry=industry,
        location=location,
        device=device
    )
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(user_input)
    
    # Export results
    monitor.export_results()
    
    print(f"\n✅ Analysis complete! Found {len(results)} keyword results.")

if __name__ == "__main__":
    main()
