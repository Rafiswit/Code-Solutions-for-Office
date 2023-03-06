import os
import pandas as pd

# Set the directory path where the Excel files are stored
folder_path = 'upload file'

# Initialize an empty list to store the DataFrames
dfs = []

# Loop through each file in the directory
for file_name in os.listdir(folder_path):

    # Check if the file is an Excel file
    if file_name.endswith('.xls') or file_name.endswith('.xlsx'):

        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        # Read the Excel file into a dictionary of DataFrames, one for each sheet
        df_dict = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')

        # Loop through each DataFrame in the dictionary
        for sheet_name, df in df_dict.items():

            # Add a column to identify the sheet name
            df['Sheet Name'] = sheet_name

            # Add a column to identify the file name
            df['File Name'] = file_name

            # Append the DataFrame to the list
            dfs.append(df)

# Concatenate all the DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined DataFrame to a new Excel file
output_file_path = 'output file to save data'

combined_df.to_excel(output_file_path, index=False)

print('All Excel files have been combined into a single sheet in the output file:', output_file_path)
