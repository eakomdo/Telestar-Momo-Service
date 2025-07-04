#!/usr/bin/env python3
"""
Simple script to read Excel data and extract customer/merchant information
"""

def read_excel_as_csv():
    """Try to read Excel files by converting them to CSV format"""
    import subprocess
    import os
    
    # Try to convert Excel to CSV using available tools
    try:
        # Try libreoffice if available
        result = subprocess.run(['libreoffice', '--headless', '--convert-to', 'csv', 'telestar_customer_list.xlsx'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("Converted customer Excel to CSV")
            
        result = subprocess.run(['libreoffice', '--headless', '--convert-to', 'csv', 'merchant_list.xlsx'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("Converted merchant Excel to CSV")
            
        # Read the CSV files
        if os.path.exists('telestar_customer_list.csv'):
            print("\n=== CUSTOMER DATA ===")
            with open('telestar_customer_list.csv', 'r') as f:
                for i, line in enumerate(f.readlines()[:10]):
                    print(f"Row {i+1}: {line.strip()}")
                    
        if os.path.exists('merchant_list.csv'):
            print("\n=== MERCHANT DATA ===")
            with open('merchant_list.csv', 'r') as f:
                for i, line in enumerate(f.readlines()[:10]):
                    print(f"Row {i+1}: {line.strip()}")
                    
    except Exception as e:
        print(f"Error converting Excel files: {e}")
        return False
    
    return True

def show_current_hardcoded_data():
    """Show what data is currently hardcoded in the application"""
    print("\n=== CURRENT HARDCODED DATA IN APPLICATION ===")
    
    # Customer data from the code
    telestar_customers = {
        "05920979359": "ABASS, Osman",
        "05923456789": "MENSAH, Kwame",
        "05934567890": "ASANTE, Grace",
        "05945678901": "OPPONG, Samuel",
        "05956789012": "BOATENG, Mary",
        "05987654321": "ADDO, Akosua",
        "05912345678": "KWAME, Kofi",
        "05965432109": "AMOAH, Ama"
    }
    
    print("\nCUSTOMER PHONE NUMBERS:")
    for phone, name in telestar_customers.items():
        print(f"  {phone} -> {name}")
    
    # Merchant data from the code
    merchants = {
        "558032": "ALL IS WELL BAKERIES",
        "123456": "TECH SOLUTIONS LTD",
        "789012": "GOLDEN FOODS",
        "345678": "EVERGREEN ENTERPRISE",
        "901234": "SMART ELECTRONICS"
    }
    
    print("\nMERCHANT IDs:")
    for merchant_id, name in merchants.items():
        print(f"  {merchant_id} -> {name}")

if __name__ == "__main__":
    print("Reading Excel data...")
    
    # Show current hardcoded data
    show_current_hardcoded_data()
    
    # Try to read actual Excel files
    if not read_excel_as_csv():
        print("\nCould not read Excel files. You may need to:")
        print("1. Install LibreOffice to convert Excel to CSV")
        print("2. Or manually check the Excel files to see what data they contain")
        print("3. Then update the hardcoded data in momo_application_with_functions.py")
