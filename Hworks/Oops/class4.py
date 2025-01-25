class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Current balance: ₹{self.balance}")

# Creating two accounts
account_one = Account(5000)
account_two = Account(2000)

# Displaying initial balances
print("Account One:")
account_one.display_balance()
print("Account Two:")
account_two.display_balance()

# Withdrawing $100 from both accounts
print("\nWithdrawing ₹100 from both accounts:")
account_one.withdraw(100)
account_two.withdraw(100)

# Displaying updated balances
print("\nUpdated Balances:")
print("Account One:")
account_one.display_balance()
print("Account Two:")
account_two.display_balance()