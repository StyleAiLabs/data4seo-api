#!/usr/bin/env python3
"""
Demo script for AI Visibility Monitor
Tests the system with sample data
"""

from ai_visibility_monitor import UserInput, AIVisibilityMonitor
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

def demo_run():
    """Run demo with sample data"""
    print("🚀 Running AI Visibility Monitor Demo")
    print("=====================================")
    
    # Demo credentials (replace with actual ones)
    login = os.getenv('DATAFORSEO_LOGIN', 'demo_login')
    password = os.getenv('DATAFORSEO_PASSWORD', 'demo_password')
    
    # Sample brand data
    demo_input = UserInput(
        brand_name="Nike",
        brand_domain="nike.com",
        competitors=["adidas.com", "puma.com", "underarmour.com"],
        serp_queries=[
            "running shoes",
            "athletic wear",
            "sports equipment",
            "basketball shoes",
            "workout clothes"
        ],
        industry="Sports & Athletic Wear",
        location="United States",
        device="desktop",
        language="English"
    )
    
    print(f"📊 Demo Parameters:")
    print(f"   Brand: {demo_input.brand_name}")
    print(f"   Domain: {demo_input.brand_domain}")
    print(f"   Competitors: {', '.join(demo_input.competitors)}")
    print(f"   Queries: {', '.join(demo_input.serp_queries)}")
    print(f"   Location: {demo_input.location}")
    print(f"   Device: {demo_input.device}")
    
    if login == 'demo_login':
        print("\n⚠️  Using demo credentials - set real credentials with:")
        print("   export DATAFORSEO_LOGIN='your_login'")
        print("   export DATAFORSEO_PASSWORD='your_password'")
        return
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(demo_input)
    
    # Export results
    monitor.export_results("results/demo_results.json")
    
    print(f"\n✅ Demo complete! Analyzed {len(results)} keywords.")

if __name__ == "__main__":
    demo_run()
