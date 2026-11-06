class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


student = Student("Ali", 7, 92)
student.display()
