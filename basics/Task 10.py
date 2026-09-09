number = int(input("Enter a 5 digit single number: "))

# Extract the last digit using modulus operator
digit1 = number % 10

# Remove the last digit
number = number // 10

# Extract the next digit
digit2 = number % 10
number = number // 10

# Extract the next digit
digit3 = number % 10
number = number // 10

# Extract the next digit
digit4 = number % 10
number = number // 10

# Extract the first digit
digit5 = number % 10

# Calculate the sum of all five digits
sum_digits = digit1 + digit2 + digit3 + digit4 + digit5

# Display the result
print("Sum of all digits of the number is:", sum_digits)