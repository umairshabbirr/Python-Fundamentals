# Program: String Operations
# Purpose: To demonstrate basic string operations

text = "Python Programming"

print("Original String:", text)

# Length of string
print("Length:", len(text))

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Replace word
print("Replace Python with AI:", text.replace("Python", "AI"))

# String slicing
print("First 6 characters:", text[0:6])

# Check substring
print("Contains 'Program':", "Program" in text)
