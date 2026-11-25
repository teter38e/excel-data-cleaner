
import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR / "Data" / "Input"
OUTPUT_DIR = BASE_DIR / "Data" / "Output"

OUTPUT_DIR.mkdir(exist_ok=True)

excel_files = list(INPUT_DIR.glob("*.xlsx"))
if not excel_files:
    print("No Excel files found in Input folder!")
    exit()

print("Available Excel files:")

for i in range(len(excel_files)):
    print(f"{i + 1}. {excel_files[i].name}")

try:
    choice = int(input("Choose a file number: "))
except ValueError:
    print("Please enter a valid number!")
    exit()
if 1 <= choice <= len(excel_files):
    FILE_PATH = excel_files[choice - 1]
    print("Selected file:", FILE_PATH.name)
else:
    print("Invalid choice!")
    exit()

# Read Excel file
df = pd.read_excel(FILE_PATH)
required_columns = ["Name", "Age", "City", "Salary"]

missing_columns = []

for column in required_columns:
    if column not in df.columns:
        missing_columns.append(column)

if missing_columns:
    print("Missing required columns:", ", ".join(missing_columns))
    exit()

print("\n\n\nOriginal rows:", len(df))
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
output_file = OUTPUT_DIR / f"{FILE_PATH.stem}_cleaned.xlsx"
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