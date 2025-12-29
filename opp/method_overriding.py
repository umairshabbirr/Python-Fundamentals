# Program: Real Life Vehicle Example
# Purpose: To demonstrate inheritance using real-life example

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

# Creating object
ecar = ElectricCar()
ecar.start()
ecar.drive()
ecar.charge()
