class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Cannot divide by zero"
        return self.num1 / self.num2

    def display(self):
        print("Calculator Results")
        print("First Number:", self.num1)
        print("Second Number:", self.num2)
        print("Addition:", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication:", self.multiply())
        print("Division:", self.divide())


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calc = Calculator(num1, num2)
calc.display()
