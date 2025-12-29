# Program: Multilevel Inheritance
# Purpose: To demonstrate multilevel inheritance in Python

class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

# Creating object
obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()
