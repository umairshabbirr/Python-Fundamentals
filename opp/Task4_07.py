class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours):
        salary = self.hourly_rate * hours
        return salary


# Creating an object
emp1 = Employee("Umair", 500)

# Calculating salary
total_salary = emp1.calculate_salary(40)

# Displaying results
print("Employee Name:", emp1.name)
print("Total Salary:", total_salary)