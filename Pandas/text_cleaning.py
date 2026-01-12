# Program: Text Cleaning
# Purpose: To clean and preprocess text data

import pandas as pd

data = {
    "Text": [" Hello World! ", "Python,Programming", " AI & ML "]
}

df = pd.DataFrame(data)

print("Original Text:")
print(df)

# Text cleaning
df["Clean_Text"] = df["Text"].str.strip()
df["Clean_Text"] = df["Clean_Text"].str.lower()
df["Clean_Text"] = df["Clean_Text"].str.replace("[^a-z ]", "", regex=True)

print("\nCleaned Text:")
print(df)
