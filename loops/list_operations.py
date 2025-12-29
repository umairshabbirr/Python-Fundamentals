# Program: List Operations
# Purpose: To demonstrate basic list operations

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Add an element
numbers.append(60)
print("After append:", numbers)

# Remove an element
numbers.remove(20)
print("After remove:", numbers)

# Access element
print("First element:", numbers[0])

# Length of list
print("Length of list:", len(numbers))

# Loop through list
print("List elements:")
for n in numbers:
    print(n)
