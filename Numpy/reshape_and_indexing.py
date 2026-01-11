# Program: Reshape and Indexing
# Purpose: To demonstrate reshaping and indexing in NumPy arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape array
reshaped_arr = arr.reshape(2, 3)

print("Original Array:", arr)
print("Reshaped Array:\n", reshaped_arr)

# Indexing
print("Element at row 0, column 1:", reshaped_arr[0][1])
print("First row:", reshaped_arr[0])
print("Second column:", reshaped_arr[:, 1])
