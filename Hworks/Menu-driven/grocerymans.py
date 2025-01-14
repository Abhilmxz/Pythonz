# user enter data store here
grocery_list = []

while True:
    print("Grocery List Manager")
    print("1. Add an item to the list")
    print("2. View the list")
    print("3. Remove an item by name")
    print("4. Clear the entire list")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

# adding  Items to the List

    if choice == "1":
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"{item} added to the list.")

# View the List  user enterd 

    elif choice == "2":
        if grocery_list:
            print("\nYour Grocery List:")
            for item in grocery_list:
                print(f"- {item}")
        else:
            print("Your grocery list is empty.")

    #Remove Item by Name here

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} has been removed from the list.")
        else:
            print(f"{item} is not in the list.")

    #Clear the user added Entire List    

    elif choice == "4":
        grocery_list.clear()
        print("The entire grocery list has been cleared.")

   #Clear the Entire List 
        
    elif choice == "5":
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")
