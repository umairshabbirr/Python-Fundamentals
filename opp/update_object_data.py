# Program: Update Object Data
# Purpose: To update object attributes after creation

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

# Create object
emp1 = Employee("Sara", 50000)
emp1.display()

# Update object data
emp1.salary = 60000

print("\nAfter Salary Update:")
emp1.display()