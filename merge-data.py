import pandas as pd
import glob
import os

# 1. Search for any Excel or CSV file in the main folder or subfolders
all_files = glob.glob("**/*.xlsx", recursive=True) + glob.glob("**/*.csv", recursive=True)

print(f"Found {len(all_files)} files to merge.")

data_list = []

for file in all_files:
    print(f"Reading file: {os.path.basename(file)}")
    # Check if the file is CSV or Excel to read it correctly
    if file.endswith('.csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    data_list.append(data)

# 2. Combine all data into a single DataFrame
if data_list:
    combined_data = pd.concat(data_list, ignore_index=True)
    
    # Save the merged data to a new Excel file
    output_file = "merged_AGE219_data.xlsx"
    combined_data.to_excel(output_file, index=False)
    
    print("\n--- SUCCESS! ---")
    print(f"All files have been successfully merged into: {output_file}")
else:
    print("No files found! Check your folders again.")