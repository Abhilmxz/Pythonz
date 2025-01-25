class Account:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

def main():
    print("Welcome to the Bank Account Management System")

    # Get initial account details
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter your initial balance: "))
    
    account = Account(account_number, initial_balance)

    while True:
        print("\nChoose an action:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Display Account Info")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':
            account.display_account_info()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()