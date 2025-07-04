
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

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

def momopay_paybill(account_balance):
    '''
    account_balance (float) : User's current account balance
    Allows customers to make payments with merchant IDs
    Returns account_balance
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

def pairtime_bundle(account_balance):
    '''
    account_balance (float) : User's current account balance
    Allows customers to buy airtime and data bundles of choice
    Returns account_balance
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

def allow_cashout(account_balance,password):
    '''
    account_balance (float) : User's current account balance
    password (int) : User' s MOMO pin
    Lets a random vendor send prompt for user to cash out a random amount
    Customers then authorize cashout prompt with pin
    Returns account_balance
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def my_wallet(account_balance, password):
    '''
    account_balance (float) : User's current account balance
    password (int) : User' s MOMO pin
    Allows users to top up, view transaction history and change pin
    Returns account_balance, password
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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

                # Main program based on user's choice, where function are called
                choice = input("Enter your choice: ")

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
