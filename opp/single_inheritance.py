# Program: Single Inheritance
# Purpose: To demonstrate single inheritance in Python

class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

# Creating object of Child class
obj = Child()
obj.show_parent()
obj.show_child()
