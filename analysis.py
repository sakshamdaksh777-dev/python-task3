import pandas as pd

# Load data
data = pd.read_csv("data.csv")

# Calculate statistics
average_marks = data["Marks"].mean()
max_marks = data["Marks"].max()
min_marks = data["Marks"].min()

print("Average Marks:", average_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)