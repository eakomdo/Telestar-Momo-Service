#!/usr/bin/env python3
"""
Script to load actual customer and merchant data from CSV files
"""


def load_customer_data():
    """Load customer data from CSV file"""
    customer_data = {}
    try:
        print("Loading customer data...")
        with open('telestar_customer_list.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Found {len(lines)} lines in customer file")
            for i, line in enumerate(lines[1:], 2):  # Skip header, start from line 2
                if line.strip():
                    parts = line.strip().split(',', 1)
                    if len(parts) >= 2:
                        phone_num = parts[0].strip().strip('"').strip("'")
                        name = parts[1].strip().strip('"').strip("'")
                        customer_data[phone_num] = name
                    else:
                        print(f"Warning: Line {i} has unexpected format: {line.strip()}")
        print(f"Successfully loaded {len(customer_data)} customers")
    except FileNotFoundError:
        print("Error: telestar_customer_list.csv not found")
    except UnicodeDecodeError as e:
        print(f"Error reading customer file - encoding issue: {e}")
    except (OSError, IOError) as e:
        print(f"Error loading customer data: {e}")
        import traceback
        traceback.print_exc()

    return customer_data

def load_merchant_data():
    """Load merchant data from CSV file"""
    merchant_data = {}
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
                        merchant_data[vendor_id] = vendor_name
                    else:
                        print(f"Warning: Line {i} has unexpected format: {line.strip()}")
        print(f"Successfully loaded {len(merchant_data)} merchants")
    except FileNotFoundError:
        print("Error: merchant_list.csv not found")
    except UnicodeDecodeError as e:
        print(f"Error reading merchant file - encoding issue: {e}")
    except (OSError, IOError) as e:
        print(f"Error loading merchant data: {e}")
        import traceback
        traceback.print_exc()

    return merchant_data

def generate_updated_code():
    """Generate the updated dictionaries for the main application"""
    customer_data = load_customer_data()
    merchant_data = load_merchant_data()

    print("=== UPDATED CUSTOMER DATA ===")
    print("telestar_customers = {")
    for phone_num, customer_name in list(customer_data.items())[:20]:  # Show first 20
        print(f'    "{phone_num}": "{customer_name}",')
    print("}")

    print("\n=== UPDATED MERCHANT DATA ===")
    print("merchants = {")
    for vendor_id, vendor_name in merchant_data.items():
        print(f'    "{vendor_id}": "{vendor_name}",')
    print("}")

    return customer_data, merchant_data

if __name__ == "__main__":
    customers, merchants = generate_updated_code()

    print(f"\nTotal customers: {len(customers)}")
    print(f"Total merchants: {len(merchants)}")

    # Show some examples for testing
    print("\n=== TEST EXAMPLES ===")
    customer_phone_list = list(customers.keys())[:5]
    print("Customer phone numbers to try:")
    for phone_number in customer_phone_list:
        print(f"  {phone_number} -> {customers[phone_number]}")

    merchant_id_list = list(merchants.keys())[:5]
    print("\nMerchant IDs to try:")
    for merchant_code in merchant_id_list:
        print(f"  {merchant_code} -> {merchants[merchant_code]}")
