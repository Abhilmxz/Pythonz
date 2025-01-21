class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("The cat meows: Meow! Meow!")

# Create objects of the derived classes
dog = Dog()
cat = Cat()

# Call the sound method for each object
dog.sound()  
cat.sound()  
