# dictionary for store user adding student data
students = {}

while True:
    # displaying menu list
    print("Student Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by roll number")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    # add a new student here the studen roll no and name
    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        students[roll_number] = name
        print("Student added successfully!")
    # here display all studens detials   
    elif choice == "2":
        if students:
            print("\nList of all students:")
            for roll_number, name in students.items():
                print(f"Name: {name}, Roll Number: {roll_number}")
        else:
            print("No students available.")
    #here we search add students   
    elif choice == "3":
        roll_number = input("Enter roll number to search: ")
        if roll_number in students:
            print(f"Student found: Name: {students[roll_number]}, Roll Number: {roll_number}")
        else:
            print("Student not found with this roll number.")
    # exit option
    elif choice == "4":
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")
