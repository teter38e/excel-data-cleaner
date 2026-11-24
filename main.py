
import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "Data" / "Input" / "sample_input.xlsx"
OUTPUT_DIR = BASE_DIR / "Data" / "Output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Read Excel file
df = pd.read_excel(FILE_PATH)

print("Original rows:", len(df))
original_rows = len(df)

# Remove duplicate rows
duplicates_count = df.duplicated().sum()
print("Duplicates found:", duplicates_count)
df = df.drop_duplicates()

cleaned_rows = len(df)
removed_rows = original_rows - cleaned_rows

print("Rows removed:", removed_rows)

missing_values = df.isnull().sum()
total_missing = missing_values.sum()

print("Missing values before cleaning:")
print(missing_values)

print("Total missing values:", total_missing)

average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)

print("\nAge after filling missing values:")
print(df["Age"])

df["City"] = df["City"].fillna("Unknown")



df["Salary"] = df["Salary"].astype("string")
df["Salary"] = df["Salary"].fillna("Unknown")

print("\nMissing values after filling:")
print(df.isnull().sum())

print("\nData after filling missing values:")
print(df)


# Save cleaned file
output_file = OUTPUT_DIR / "cleaned_data.xlsx"
df.to_excel(output_file, index=False)

print("\nCleaning completed!")
print("Saved to:", output_file)





print("\n========== CLEANING REPORT ==========")

print(f"Original rows: {original_rows}")
print(f"Duplicates removed: {duplicates_count}")
print(f"Missing values found: {total_missing}")
print(f"Rows removed: {removed_rows}")
print(f"Final rows: {len(df)}")

print("=====================================")