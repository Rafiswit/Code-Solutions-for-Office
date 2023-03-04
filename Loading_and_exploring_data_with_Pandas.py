import pandas as pd

# Load a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Display summary statistics for numerical columns
print(df.describe())

# Count the number of rows in the DataFrame
print(len(df))

# Select a subset of the data based on a condition
subset = df[df['age'] > 30]
