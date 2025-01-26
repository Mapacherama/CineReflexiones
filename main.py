import pandas as pd

# Load the CSV file into a DataFrame
file_path = "data\movies_metadata.csv"  # Replace with your file's path
movies = pd.read_csv(file_path)

# Display basic information about the dataset
print("\nDataset Info:")
print(movies.info())

# Display the first few rows of the dataset
print("\nFirst 5 rows:")
print(movies.head())

# Display basic statistics of numerical columns
print("\nBasic statistics:")
print(movies.describe())

# Display column names
print("\nColumns in the dataset:")
print(movies.columns.tolist())
