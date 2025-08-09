#!/usr/bin/env python3
"""
Real Business Test: Analyze AI Visibility for a Brand using Informational Queries
"""

import sys
import time
from ai_visibility_monitor import AIVisibilityMonitor, UserInput

def run_business_test():
    """Test the full user journey with AI Overview triggering keywords"""
    
    # Load credentials
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    # Get credentials
    login = os.getenv('DATAFORSEO_LOGIN')
    password = os.getenv('DATAFORSEO_PASSWORD')
    
    if not login or not password:
        print("❌ Missing credentials! Please set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD in .env file")
        return
    
    print("🏥 Business Case: Health & Wellness Brand AI Visibility")
    print("=" * 60)
    
    # Create realistic business scenario
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
    
    # Run analysis
    monitor = AIVisibilityMonitor(login, password)
    results = monitor.run_analysis(user_input)
    
    # Show summary
    print(f"\n📋 SUMMARY REPORT")
    print("=" * 30)
    monitor.print_summary()

if __name__ == "__main__":
    run_business_test()
