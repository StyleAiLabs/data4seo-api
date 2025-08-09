#!/usr/bin/env python3
"""
Quick test with minimal keywords to verify fixes
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

def quick_test():
    """Quick test with just 1 keyword"""
    print("🚀 Quick AI Visibility Test")
    print("===========================")
    
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ No credentials found")
        return
    
    test_input = UserInput(
        brand_name="Nike",
        brand_domain="nike.com", 
        competitors=["adidas.com"],
        serp_queries=["running shoes"],  # Just 1 keyword for quick test
        industry="Sports",
        location="United States",
        device="desktop"
    )
    
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(test_input)
    
    print(f"\n✅ Test complete! Results: {len(results)} keywords analyzed")

if __name__ == "__main__":
    quick_test()
