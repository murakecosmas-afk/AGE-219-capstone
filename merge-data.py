import pandas as pd
import glob

# 1. Read all CSV files from the DATA folder
files = glob.glob("DATA/*.csv")

# 2. Merge all files into a single DataFrame
df_list = [pd.read_csv(f) for f in files]
merged_df = pd.concat(df_list, ignore_index=True)

# 3. Save the merged result
merged_df.to_csv("final_merged_data.csv", index=False)
print("Data has been successfully merged into 'final_merged_data.csv'!")