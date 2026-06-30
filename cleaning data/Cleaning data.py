import pandas as pd

# 1. Load the file
df = pd.read_excel("merged_AGE219_data.xlsx")

# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 3. Handle duplicates: Keep only the first occurrence of columns
df = df.loc[:, ~df.columns.duplicated()]

# 4. Clean: Drop rows where 'year' is empty
df = df.dropna(subset=['year'])

# 5. Group and Calculate Mean
# Replace 'moisture1' with the exact name from your column list if needed
yearly_mean = df.groupby('year')['moisture1'].mean()

print("--- MEAN MOISTURE PER YEAR ---")
print(yearly_mean)