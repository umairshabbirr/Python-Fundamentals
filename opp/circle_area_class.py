# Program: Circle Area using Class
# Purpose: To calculate area of a circle using class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Creating object
circle1 = Circle(5)
area = circle1.calculate_area()

print("Radius:", circle1.radius)
print("Area of Circle:", area)
