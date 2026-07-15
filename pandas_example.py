import pandas as pd

# Load your dataset with the correct filename
df = pd.read_csv('dataset.csv')

print("=== MY NEW DATASET SUCCESSFULLY LOADED ===\n")
print(df)

# Quick Analysis
print("\n=== QUICK STATS ===")
print(f"Total Students: {len(df)}")
print(f"Average Marks: {df['Marks'].mean():.1f}")
print(f"Highest Mark: {df['Marks'].max()} ({df.loc[df['Marks'].idxmax(), 'Name']})")