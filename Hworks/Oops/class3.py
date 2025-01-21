class Person:
    def __init__(self, name, age):

        # a Person with name and age.

        self.name = name
        self.age = age

class Employee:
    def __init__(self, emp_id, salary):
        
        #an Employee with emp_id and salary.

        self.emp_id = emp_id
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        
        # Create a Manager with attributes from both Person and Employee, and add department.
     
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_details(self):
        
        # Display all the attributes of the Manager.
    
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")

# Create an object of the Manager class
manager = Manager(name="Alice Johnson", age=40, emp_id="M1234", salary=85000, department="IT")

# Display all the attributes of the Manager
manager.display_details()
