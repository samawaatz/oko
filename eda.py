import pandas as pd

# Read dataset
file_path = 'soil_data.csv'
df = pd.read_csv(file_path)

# Column overview
print("\nColumns:\n", df.columns.tolist())

# Missing values per column
print("\nMissing values:\n", df.isnull().sum())

# Summary statistics (numeric only by default)
print("\nSummary statistics:\n", df.describe(include='all'))

# Class distribution for SoilType
if 'SoilType' in df.columns:
    print("\nClass distribution:\n", df['SoilType'].value_counts())
else:
    print("\n'SoilType' column not found for class distribution")

