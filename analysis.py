import pandas as pd
df = pd.read_excel("merged_AGE219_data.xlsx")
print(df.head())
print(df["moisture0"].mean())
print(df["Year"].unique())
print(df["Year"].value_counts())