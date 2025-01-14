# user enter data store here
balance = 0

while True:
    print("Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    # checking balance here
    if choice == "1":
        print(f"Your current balance is: ₹{balance}")
    # cash deposit option here
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"₹{amount} deposited successfully. Your new balance is: ₹{balance}")
    # money withdraw option here
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully. Your new balance is: ₹{balance}")
        else:
            print("Insufficient funds.")
    # exit
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
