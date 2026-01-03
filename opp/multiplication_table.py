# Program: Multiplication Table
# Purpose: To print multiplication table of a given number

num = int(input("Enter a number: "))

print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
