import pandas as pd
import matplotlib.pyplot as plt

# 1. Setup the student data
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Score': [85, 42, 93, 71, 55, 88]
}
df = pd.DataFrame(data)

# 2. Calculate the average score
average_score = df['Score'].mean()

# 3. Create the bar chart using Matplotlib
plt.figure(figsize=(8, 5)) # Set the size of the graph window
colors = ['green' if score > average_score else 'red' for score in df['Score']]

# Draw the bars (X-axis = Students, Y-axis = Scores)
plt.bar(df['Student'], df['Score'], color=colors, edgecolor='black')

# Add a dashed line showing the class average
plt.axhline(y=average_score, color='blue', linestyle='--', label=f'Average ({average_score:.1f})')

# 4. Add labels, title, and legend
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Student Test Scores (Above Avg = Green, Below Avg = Red)')
plt.ylim(0, 100) # Force the Y-axis to go from 0 to 100
plt.legend()

# 5. Display the window containing the chart
plt.show()