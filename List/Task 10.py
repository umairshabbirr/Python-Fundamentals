students = {
    "Ali": 85,
    "Ahmed": 78,
    "Usman": 92,
    "Hassan": 88,
    "Bilal": 75
}

name = input("Enter student's name: ")

if name in students:
    print(name, "got", students[name], "marks")
else:
    print("Student not found")