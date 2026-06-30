import pandas as pd
import matplotlib.pyplot as plt

# Load the merged data
df = pd.read_excel("merged_AGE219_data.xlsx")
df['year'] = pd.to_numeric(df['year'], errors='coerce')
yearly_mean = df.groupby('year')['moisture1'].mean()

# Prepare three subplots (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Bar Chart
yearly_mean.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Bar Chart: Mean Moisture')

# 2. Scatter Plot
axes[1].scatter(yearly_mean.index, yearly_mean.values, color='red')
axes[1].set_title('Scatter Plot: Yearly Trend')
axes[1].grid(True)

# 3. Line Plot
yearly_mean.plot(kind='line', ax=axes[2], marker='o', color='green', linestyle='-')
axes[2].set_title('Line Plot: Trend Over Years')
axes[2].grid(True)

# Save the visualization as a file
plt.tight_layout()
plt.savefig('moisture_trends.png')
print("Visualization saved as 'moisture_trends.png'")

# Optional: Show it on your screen
plt.show()