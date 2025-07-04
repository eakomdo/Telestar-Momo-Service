
# Problem Set 2, MOMO Application with Functions

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


#Description of functions to be implemented:

def transfer_money(account_balance, password):
    '''
    account_balance (float) : User's current account balance
    password (int) : User' s MOMO pin
    Transfers an amount to a Telestar customer after authorization
    Returns account_balance
    '''
    
    # Telestar customer database (sample data)
    telestar_customers = {
        "05920979359": "ABASS, Osman",
        "05923456789": "MENSAH, Kwame",
        "05934567890": "ASANTE, Grace",
        "05945678901": "OPPONG, Samuel",
        "05956789012": "BOATENG, Mary"
    }
    
    print("Transfer Money:")
    print("1. TeleStar Network")
    print("2. Other Networks")
    
    while True:
        try:
            choice = input("Enter your transfer choice: ")
            if choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except:
            print("Invalid input. Please try again.")
    
    if choice == "1":
        # TeleStar Network Transfer
        while True:
            phone = input("Enter the recipient's TeleStar phone number (should start with 059): ")
            if phone.startswith("059") and len(phone) == 10:
                verify_phone = input("Verify the phone number by entering it again: ")
                if phone == verify_phone:
                    break
                else:
                    print("Phone numbers don't match. Please try again.")
            else:
                print("Invalid phone number. Must start with 059 and be 11 digits long.")
        
        # Check if phone exists in Telestar network
        if phone not in telestar_customers:
            print("Phone number not found in TeleStar network.")
            return account_balance
        
        customer_name = telestar_customers[phone]
        
        # Get transfer amount
        while True:
            try:
                amount = float(input("Enter the amount to transfer: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                if amount > account_balance:
                    print("Insufficient balance.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        # PIN authorization
        while True:
            pin = input(f"Enter your MOMO pin to authorize transfer to {customer_name}: ")
            if pin == password:
                break
            else:
                print("Invalid PIN. Please try again.")
        
        # Calculate charges
        e_levy = amount * 0.01  # 1% E-levy
        service_charge = 0.2    # Fixed service charge
        total_deduction = amount + e_levy + service_charge
        
        if total_deduction > account_balance:
            print("Insufficient balance for transaction charges.")
            return account_balance
        
        # Process transfer
        account_balance -= total_deduction
        
        print(f"GHS {amount} has been sent successfully to {customer_name}, with E-levy charge of GHS{e_levy:.1f}")
        print(f"Service charge: GHS {service_charge}")
        print(f"New balance: GHS {account_balance:.1f}")
        
    else:
        # Other Networks Transfer (simplified implementation)
        phone = input("Enter the recipient's phone number: ")
        
        while True:
            try:
                amount = float(input("Enter the amount to transfer: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                if amount > account_balance:
                    print("Insufficient balance.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        # PIN authorization
        while True:
            pin = input("Enter your MOMO pin to authorize transfer: ")
            if pin == password:
                break
            else:
                print("Invalid PIN. Please try again.")
        
        # Calculate charges (higher for other networks)
        e_levy = amount * 0.01  # 1% E-levy
        service_charge = 0.5    # Higher service charge for other networks
        total_deduction = amount + e_levy + service_charge
        
        if total_deduction > account_balance:
            print("Insufficient balance for transaction charges.")
            return account_balance
        
        # Process transfer
        account_balance -= total_deduction
        
        print(f"GHS {amount} has been sent successfully to {phone}, with E-levy charge of GHS{e_levy:.1f}")
        print(f"Service charge: GHS {service_charge}")
        print(f"New balance: GHS {account_balance:.1f}")
    
    return account_balance

def momopay_paybill(account_balance):
    '''
    account_balance (float) : User's current account balance
    Allows customers to make payments with merchant IDs
    Returns account_balance
    '''
    
    # Merchant database (sample data)
    merchants = {
        "558032": "ALL IS WELL BAKERIES",
        "123456": "TECH SOLUTIONS LTD",
        "789012": "GOLDEN FOODS",
        "345678": "EVERGREEN ENTERPRISE",
        "901234": "SMART ELECTRONICS"
    }
    
    print("MomoPay/Paybill:")
    
    while True:
        merchant_id = input("Enter the 6-digit Merchant ID: ")
        if len(merchant_id) == 6 and merchant_id.isdigit():
            if merchant_id in merchants:
                merchant_name = merchants[merchant_id]
                print(f"Proceed to make payment to merchant, {merchant_name}")
                break
            else:
                print("Merchant ID not found. Please try again.")
        else:
            print("Invalid Merchant ID. Must be 6 digits.")
    
    # Get payment amount
    while True:
        try:
            amount = float(input("Enter the amount to pay: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            if amount > account_balance:
                print("Insufficient balance.")
                return account_balance
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    # Calculate E-levy (1% for MomoPay, no service charge)
    e_levy = amount * 0.01
    total_deduction = amount + e_levy
    
    if total_deduction > account_balance:
        print("Insufficient balance for E-levy charge.")
        return account_balance
    
    # Process payment
    account_balance -= total_deduction
    
    print(f"GHS {amount} has been paid successfully to {merchant_name}, with E-levy charge of GHS {e_levy:.1f}.")
    print(f"New balance: GHS {account_balance:.1f}")
    
    return account_balance

def airtime_bundle(account_balance):
    '''
    account_balance (float) : User's current account balance
    Allows customers to buy airtime and data bundles of choice
    Returns account_balance
    '''
    
    print("Airtime and Bundles:")
    print("1. Buy Airtime")
    print("2. Buy Bundles")
    
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except:
            print("Invalid input. Please try again.")
    
    if choice == "1":
        # Buy Airtime
        while True:
            try:
                amount = float(input("Enter airtime amount: GHS "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                if amount > account_balance:
                    print("Insufficient balance.")
                    return account_balance
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        # Process airtime purchase
        account_balance -= amount
        print(f"GHS {amount} airtime successfully purchased.")
        print(f"New balance: GHS {account_balance:.1f}")
    
    elif choice == "2":
        # Buy Bundles
        print("Bundles:")
        print("1. GHC 5 (280 MB)")
        print("2. GHC 10 (667 MB)")
        print("3. GHC 100 (10 GB)")
        print("4. Flexi-Bundle (GHS 0 - GHS 400)")
        
        while True:
            try:
                bundle_choice = input("Choose your bundle type: ")
                if bundle_choice in ["1", "2", "3", "4"]:
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except:
                print("Invalid input. Please try again.")
        
        if bundle_choice == "1":
            # GHC 5 bundle
            amount = 5.0
            data_mb = 280
            if amount > account_balance:
                print("Insufficient balance.")
                return account_balance
            account_balance -= amount
            print(f"{data_mb} MB Data Bundle successfully purchased.")
            print(f"New balance: GHS {account_balance:.1f}")
        
        elif bundle_choice == "2":
            # GHC 10 bundle
            amount = 10.0
            data_mb = 667
            if amount > account_balance:
                print("Insufficient balance.")
                return account_balance
            account_balance -= amount
            print(f"{data_mb} MB Data Bundle successfully purchased.")
            print(f"New balance: GHS {account_balance:.1f}")
        
        elif bundle_choice == "3":
            # GHC 100 bundle
            amount = 100.0
            data_gb = 10
            if amount > account_balance:
                print("Insufficient balance.")
                return account_balance
            account_balance -= amount
            print(f"{data_gb} GB Data Bundle successfully purchased.")
            print(f"New balance: GHS {account_balance:.1f}")
        
        elif bundle_choice == "4":
            # Flexi-Bundle
            while True:
                try:
                    amount = float(input("Enter amount to purchase: "))
                    if amount < 0 or amount > 400:
                        print("Amount must be between GHS 0 and GHS 400.")
                        continue
                    if amount > account_balance:
                        print("Insufficient balance.")
                        return account_balance
                    break
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            
            # Calculate data using the given formula
            cost_per_mb = 0.01786
            base_data_mb = amount / cost_per_mb
            bonus_data_mb = base_data_mb * 0.05  # 5% bonus
            total_data_mb = base_data_mb + bonus_data_mb
            
            account_balance -= amount
            print(f"{total_data_mb:.1f} MB Data Bundle successfully purchased.")
            print(f"New balance: GHS {account_balance:.1f}")
    
    return account_balance

def allow_cashout(account_balance, password):
    '''
    account_balance (float) : User's current account balance
    password (int) : User' s MOMO pin
    Lets a random vendor send prompt for user to cash out a random amount
    Customers then authorize cashout prompt with pin
    Returns account_balance
    '''
    
    import random
    
    # Merchant database (same as momopay)
    merchants = {
        "558032": "ALL IS WELL BAKERIES",
        "123456": "TECH SOLUTIONS LTD",
        "789012": "GOLDEN FOODS",
        "345678": "EVERGREEN ENTERPRISE",
        "901234": "SMART ELECTRONICS"
    }
    
    print("Allow CashOut:")
    print("1. Yes")
    print("2. No")
    
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice in ["1", "2"]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except:
            print("Invalid input. Please try again.")
    
    if choice == "2":
        print("CashOut cancelled.")
        return account_balance
    
    # Generate random cashout scenario
    random_merchants = list(merchants.values())
    random_merchant = random.choice(random_merchants)
    
    # Generate random amount (between 10 and min(account_balance, 500))
    max_amount = min(account_balance, 500)
    if max_amount < 10:
        print("Insufficient balance for cashout.")
        return account_balance
    
    random_amount = random.randint(10, int(max_amount))
    
    print(f"Cashout for GHS{random_amount} to {random_merchant}")
    
    # PIN authorization
    while True:
        pin = input("Enter your MOMO PIN to authorize CashOut: ")
        if pin == password:
            break
        else:
            print("Invalid PIN. Please try again.")
    
    # Calculate cashout fee (5% of amount)
    cashout_fee = random_amount * 0.05
    total_deduction = random_amount + cashout_fee
    
    if total_deduction > account_balance:
        print("Insufficient balance for cashout fee.")
        return account_balance
    
    # Process cashout
    account_balance -= total_deduction
    
    print(f"Cash Out made for GHS {random_amount:.2f} to {random_merchant}. CashOut Fee GHS{cashout_fee:.2f} was charged automatically from your wallet.")
    print(f"Current Balance: GHS{account_balance:.2f}")
    
    return account_balance



def my_wallet(account_balance, password):
    '''
    account_balance (float) : User's current account balance
    password (int) : User' s MOMO pin
    Allows users to top up, view transaction history and change pin
    Returns account_balance, password
    '''
    
    # Global variable to store transaction history
    if not hasattr(my_wallet, 'transaction_history'):
        my_wallet.transaction_history = []
    
    print("My Wallet:")
    print("1. Top Up Balance")
    print("2. Check Balance")
    print("3. Change MoMo Pin")
    print("4. Transaction History")
    
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except:
            print("Invalid input. Please try again.")
    
    if choice == "1":
        # Top Up Balance
        while True:
            try:
                amount = float(input("Enter amount to top up your balance: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        account_balance += amount
        print(f"Balance top up is successful. New balance: GHS {account_balance:.1f}")
        
        # Record transaction
        import datetime
        transaction = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "Account Topup",
            "amount": amount,
            "charges": 0.00,
            "balance_after": account_balance,
            "status": "Success",
            "recipient": "Owner"
        }
        my_wallet.transaction_history.append(transaction)
    
    elif choice == "2":
        # Check Balance
        print(f"Current Balance: GHS {account_balance:.1f}")
    
    elif choice == "3":
        # Change MoMo Pin
        while True:
            current_pin = input("Enter your MoMo Pin: ")
            if current_pin == password:
                break
            else:
                print("Invalid current PIN. Please try again.")
        
        while True:
            new_pin = input("Enter your new 4-digit MoMo Pin: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                password = new_pin
                print("MOMO Pin successfully changed!")
                break
            else:
                print("Invalid PIN. Must be 4 digits.")
    
    elif choice == "4":
        # Transaction History
        print("Transaction History:")
        print("-" * 79)
        
        if not my_wallet.transaction_history:
            print("No transactions found.")
        else:
            for transaction in my_wallet.transaction_history:
                print(f"Timestamp    : {transaction['timestamp']}")
                print(f"Type         : {transaction['type']}")
                print(f"Amount (GHS) : {transaction['amount']:.2f}")
                print(f"Charges (GHS): {transaction['charges']:.2f}")
                print(f"Balance After: {transaction['balance_after']:.2f}")
                print(f"Status       : {transaction['status']}")
                print(f"Recipient    : {transaction['recipient']}")
                print("-" * 79)
    
    return account_balance, password



def main():
    current_balance = 1000  # Starting balance
    MOMO_pin = "7209"  # User's 4-digit MOMO PIN
    start = True
    attempt = 0
    while start:

        hashcode = input("Enter the TeleStar code: ")
        # Check if the entered code is correct
        if hashcode == "*170#":
            while True:

                # Display main menu
                print("Welcome to TeleStar Mobile Money! Please select an option:")
                print("1. Transfer Money")
                print("2. MOMO Pay")
                print("3. Airtime and Bundles")
                print("4. Allow Cash Out")
                print("5. My Wallet")

                # Main program based on user's choice, where functions are called
                choice = input("Enter your choice: ")

                if choice == "1":
                    current_balance = transfer_money(current_balance, MOMO_pin)
                elif choice == "2":
                    current_balance = momopay_paybill(current_balance)
                elif choice == "3":
                    current_balance = airtime_bundle(current_balance)
                elif choice == "4":
                    current_balance = allow_cashout(current_balance, MOMO_pin)
                elif choice == "5":
                    current_balance, MOMO_pin = my_wallet(current_balance, MOMO_pin)
                else:
                    print("Invalid choice. Please try again.")
                    continue

                # Ask if user wants to continue or exit
                exit_response = input("Do you want to perform another operation? (yes/no): ")
                if exit_response.lower() != "yes":
                    print("Thank you for using our service!")
                    start = False
                    break
        else:
            print("Invalid short code. Please try again.")
            attempt += 1
        if attempt == 3:
            start = False
            print(f"You have exhausted the maximum number of {attempt} attempts. Please restart the program")


if __name__ == "__main__":
    main()
