# Program: Statistical Functions in NumPy
# Purpose: To calculate basic statistics using NumPy

import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum Value:", np.min(data))
print("Maximum Value:", np.max(data))
