import pandas_example as pd

# 1. Create a simple dataset using a Dictionary
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Score': [85, 42, 93, 71, 55, 88]
}

# Convert the dataset into a Pandas DataFrame (a structured table)
df = pd.DataFrame(data)
print("--- Full Student Dataset ---")
print(df)
print("-" * 28)

# 2. Calculate the average score
average_score = df['Score'].mean()
print(f"\nThe class average is: {average_score:.1f}\n")

# 3. Filter and show only students who scored above average
above_average_df = df[df['Score'] > average_score]

print("--- Students Above Average ---")
print(above_average_df)