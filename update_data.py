#!/usr/bin/env python3
"""
Script to load actual customer and merchant data from CSV files
"""


def load_customer_data():
    """Load customer data from CSV file"""
    customers = {}
    try:
        print("Loading customer data...")
        with open('telestar_customer_list.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Found {len(lines)} lines in customer file")
            for i, line in enumerate(lines[1:], 2):  # Skip header, start from line 2
                if line.strip():
                    parts = line.strip().split(',', 1)
                    if len(parts) >= 2:
                        phone = parts[0].strip().strip('"').strip("'")
                        name = parts[1].strip().strip('"').strip("'")
                        customers[phone] = name
                    else:
                        print(f"Warning: Line {i} has unexpected format: {line.strip()}")
        print(f"Successfully loaded {len(customers)} customers")
    except FileNotFoundError:
        print("Error: telestar_customer_list.csv not found")
    except UnicodeDecodeError as e:
        print(f"Error reading customer file - encoding issue: {e}")
    except Exception as e:
        print(f"Unexpected error loading customer data: {e}")
        import traceback
        traceback.print_exc()
    
    return customers

def load_merchant_data():
    """Load merchant data from CSV file"""
    merchants = {}
    try:
        print("Loading merchant data...")
        with open('merchant_list.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Found {len(lines)} lines in merchant file")
            for i, line in enumerate(lines[1:], 2):  # Skip header, start from line 2
                if line.strip():
                    parts = line.strip().split(',', 1)
                    if len(parts) >= 2:
                        vendor_id = parts[0].strip().strip('"').strip("'")
                        vendor_name = parts[1].strip().strip('"').strip("'")
                        merchants[vendor_id] = vendor_name
                    else:
                        print(f"Warning: Line {i} has unexpected format: {line.strip()}")
        print(f"Successfully loaded {len(merchants)} merchants")
    except FileNotFoundError:
        print("Error: merchant_list.csv not found")
    except UnicodeDecodeError as e:
        print(f"Error reading merchant file - encoding issue: {e}")
    except Exception as e:
        print(f"Unexpected error loading merchant data: {e}")
        import traceback
        traceback.print_exc()
    
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
