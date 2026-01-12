# Program: Handling Missing Values
# Purpose: To detect and handle missing values using Pandas

import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", "Ahmed", None],
    "Age": [20, None, 19, 22],
    "Marks": [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Name"].fillna("Unknown", inplace=True)

print("\nAfter Handling Missing Values:")
print(df)
