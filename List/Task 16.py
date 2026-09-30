people = {
    "Ali": 20,
    "Ahmed": 17,
    "Usman": 22,
    "Hassan": 16,
    "Bilal": 25
}

print("People above 18 years old:")

for name, age in people.items():
    if age > 18:
        print(name, "-", age)