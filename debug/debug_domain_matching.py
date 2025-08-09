#!/usr/bin/env python3
"""
Debug Domain Matching Logic
"""

def debug_domain_matching():
    """Debug the exact domain matching that's failing"""
    
    # Test data from our debug output
    brand_domain = "mayoclinic.org"
    found_domain = "www.mayoclinic.org"
    
    print("🔍 Domain Matching Debug")
    print("=" * 30)
    
    print(f"Brand domain: '{brand_domain}'")
    print(f"Found domain: '{found_domain}'")
    
    # Current logic in the code
    brand_clean = brand_domain.lower().replace('www.', '')
    found_clean = found_domain.lower().replace('www.', '')
    
    print(f"\nAfter .replace('www.', ''):")
    print(f"Brand clean: '{brand_clean}'")
    print(f"Found clean: '{found_clean}'")
    
    # Test the comparison
    exact_match = found_domain == brand_clean
    print(f"\nExact match test: {found_domain} == {brand_clean} = {exact_match}")
    
    # The problem: we're comparing the original found_domain with cleaned brand_domain
    # But we should be comparing both cleaned domains!
    
    print(f"\n🔧 FIXED comparison:")
    print(f"found_clean == brand_clean: {found_clean} == {brand_clean} = {found_clean == brand_clean}")
    
    # Also test what our current logic is doing wrong
    print(f"\n❌ Current broken logic:")
    print(f"found_domain == brand_clean: {found_domain} == {brand_clean} = {found_domain == brand_clean}")

if __name__ == "__main__":
    debug_domain_matching()
