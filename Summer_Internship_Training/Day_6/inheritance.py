# Define the parent class to hold general data

class Vehicle:
    # The initializer method runs automatically when an object is created
    def __init__(self, brand, year):
        self.brand = brand  # Public attribute for the vehicle's brand. Stores in instance variable
        self.year = year    # Public attribute for the vehicle's manufacturing year
    
    # A method that format and restores the vehicle details as a string
    def display_info(self):
        return f"{self.brand} ({self.year})"
    
# Define a child that automatically inherits from the parent class Vehicle
class Car(Vehicle):
    # "Pass" is placeholder showing the vehicle information is inherited from the parent class
    pass

# Create an object of the Car class
# Then automatically call the __init__ method inherited from Vehicle

my_car = Car("Toyota", 2020)

# Calling the display info method inherited from the parent class Vehicle
print(my_car.display_info())  # Output: Toyota (2020)

class Animal:
    def __init__(self, species, region):
        self.species = species
        self.region = region
    
    def display_info(self):
        return f"{self.species} is found in {self.region}"
    
    
class typeOfAnimal(Animal):
    pass

animal1 = typeOfAnimal("Bengal Tiger", "India")

print(animal1.display_info())