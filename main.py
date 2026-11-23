
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

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print("Cleaned rows:", len(df))

# Save cleaned file
output_file = OUTPUT_DIR / "cleaned_data.xlsx"
df.to_excel(output_file, index=False)

print("\nCleaning completed!")
print("Saved to:", output_file)
