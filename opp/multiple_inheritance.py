# Program: Multiple Inheritance
# Purpose: To demonstrate multiple inheritance in Python

class Father:
    def father_info(self):
        print("Father class")

class Mother:
    def mother_info(self):
        print("Mother class")

class Child(Father, Mother):
    def child_info(self):
        print("Child class")

# Creating object
obj = Child()
obj.father_info()
obj.mother_info()
obj.child_info()
