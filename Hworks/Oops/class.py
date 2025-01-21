class Person:
    def __init__(self, name, age, gender):
        """
        Initialize a Person object with name, age, and gender.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        """
        Display the details of the person.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Create an object of the Person class
person = Person(name="John Doe", age=30, gender="Male")

# Display the person's details
person.display_details()
