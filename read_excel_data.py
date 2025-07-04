#!/usr/bin/env python3
"""
Simple script to read Excel data and extract customer/merchant information
"""


def read_excel_as_csv():
    """Try to read Excel files by converting them to CSV format"""
    import subprocess
    import os

    print("Attempting to convert Excel files to CSV...")

    # Try to convert Excel to CSV using available tools
    try:
        # Check if libreoffice is available
        check_result = subprocess.run(['which', 'libreoffice'],
                                      capture_output=True, text=True, check=False)
        if check_result.returncode != 0:
            print("LibreOffice not found. Trying alternative methods...")
            return False

        print("LibreOffice found. Converting files...")

        # Try libreoffice conversion
        result1 = subprocess.run(['libreoffice', '--headless', '--convert-to', 'csv',
                                 'telestar_customer_list.xlsx'],
                                 capture_output=True, text=True, timeout=30, check=False)
        if result1.returncode == 0:
            print("✓ Converted customer Excel to CSV")
        else:
            print(f"✗ Failed to convert customer Excel: {result1.stderr}")

        result2 = subprocess.run(['libreoffice', '--headless', '--convert-to', 'csv',
                                 'merchant_list.xlsx'],
                                 capture_output=True, text=True, timeout=30, check=False)
        if result2.returncode == 0:
            print("✓ Converted merchant Excel to CSV")
        else:
            print(f"✗ Failed to convert merchant Excel: {result2.stderr}")

        # Read the CSV files with proper encoding
        if os.path.exists('telestar_customer_list.csv'):
            print("\n=== CUSTOMER DATA ===")
            try:
                with open('telestar_customer_list.csv', 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:10]
                    for i, line in enumerate(lines):
                        print(f"Row {i+1}: {line.strip()}")
            except UnicodeDecodeError:
                print("Encoding issue with customer CSV. Trying different encoding...")
                with open('telestar_customer_list.csv', 'r', encoding='latin-1') as f:
                    lines = f.readlines()[:10]
                    for i, line in enumerate(lines):
                        print(f"Row {i+1}: {line.strip()}")
        else:
            print("Customer CSV file not found after conversion")

        if os.path.exists('merchant_list.csv'):
            print("\n=== MERCHANT DATA ===")
            try:
                with open('merchant_list.csv', 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:10]
                    for i, line in enumerate(lines):
                        print(f"Row {i+1}: {line.strip()}")
            except UnicodeDecodeError:
                print("Encoding issue with merchant CSV. Trying different encoding...")
                with open('merchant_list.csv', 'r', encoding='latin-1') as f:
                    lines = f.readlines()[:10]
                    for i, line in enumerate(lines):
                        print(f"Row {i+1}: {line.strip()}")
        else:
            print("Merchant CSV file not found after conversion")

    except subprocess.TimeoutExpired:
        print("Error: LibreOffice conversion timed out")
        return False
    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e}")
        return False
    except PermissionError as e:
        print(f"Error: Permission denied - {e}")
        return False
    except (OSError, subprocess.SubprocessError) as e:
        print(f"Unexpected error converting Excel files: {e}")
        import traceback
        traceback.print_exc()
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
