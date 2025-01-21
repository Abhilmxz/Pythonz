class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an object of the Car class
car = Car(brand="Toyota", model="Camry", year=2022)

# Display the car's information
car.car_info()
