class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_car(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Manufacturing Year:", self.year)

# Creating object
car1 = Car("Toyota", "Corolla", 2022)
car1.display_car()
