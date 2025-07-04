#!/usr/bin/env python3
"""
Script to load actual customer and merchant data from CSV files
"""

def load_customer_data():
    """Load customer data from CSV file"""
    customers = {}
    try:
        with open('telestar_customer_list.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                if line.strip():
                    parts = line.strip().split(',', 1)
                    if len(parts) >= 2:
                        phone = parts[0].strip()
                        name = parts[1].strip().strip('"')
                        customers[phone] = name
    except Exception as e:
        print(f"Error loading customer data: {e}")
    
    return customers

def load_merchant_data():
    """Load merchant data from CSV file"""
    merchants = {}
    try:
        with open('merchant_list.csv', 'r') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                if line.strip():
                    parts = line.strip().split(',', 1)
                    if len(parts) >= 2:
                        vendor_id = parts[0].strip()
                        vendor_name = parts[1].strip().strip('"')
                        merchants[vendor_id] = vendor_name
    except Exception as e:
        print(f"Error loading merchant data: {e}")
    
    return merchants

def generate_updated_code():
    """Generate the updated dictionaries for the main application"""
    customers = load_customer_data()
    merchants = load_merchant_data()
    
    print("=== UPDATED CUSTOMER DATA ===")
    print("telestar_customers = {")
    for phone, name in list(customers.items())[:20]:  # Show first 20
        print(f'    "{phone}": "{name}",')
    print("}")
    
    print("\n=== UPDATED MERCHANT DATA ===")
    print("merchants = {")
    for vendor_id, vendor_name in merchants.items():
        print(f'    "{vendor_id}": "{vendor_name}",')
    print("}")
    
    return customers, merchants

if __name__ == "__main__":
    customers, merchants = generate_updated_code()
    
    print(f"\nTotal customers: {len(customers)}")
    print(f"Total merchants: {len(merchants)}")
    
    # Show some examples for testing
    print("\n=== TEST EXAMPLES ===")
    customer_phones = list(customers.keys())[:5]
    print("Customer phone numbers to try:")
    for phone in customer_phones:
        print(f"  {phone} -> {customers[phone]}")
    
    merchant_ids = list(merchants.keys())[:5]
    print("\nMerchant IDs to try:")
    for merchant_id in merchant_ids:
        print(f"  {merchant_id} -> {merchants[merchant_id]}")
