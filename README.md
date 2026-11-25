# Excel Data Cleaner

A Python tool that automatically cleans Excel files using Pandas.

## Features

- Automatically finds Excel files in the `Data/Input` folder.
- Allows users to select an Excel file from a numbered menu.
- Checks whether the Input folder contains Excel files.
- Validates required columns (`Name`, `Age`, `City`, `Salary`).
- Detects and removes duplicate rows.
- Detects missing values.
- Fills missing `Age` values with the column average.
- Fills missing `City` and `Salary` values with `"Unknown"`.
- Handles invalid user input.
- Validates file selection.
- Generates a cleaning report.
- Saves cleaned files with unique names.

## Technologies

- Python
- Pandas
- OpenPyXL
- pathlib

## Project Structure

```text
excel-data-cleaner/
│
├── Data/
│   ├── Input/
│   └── Output/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/teter38e/excel-data-cleaner.git
```

2. Open the project folder:

```bash
cd excel-data-cleaner
```

3. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

1. Place your Excel files (`.xlsx`) inside the `Data/Input` folder.
2. Run the program:

```bash
python main.py
```

3. Select a file from the numbered menu.
4. The program validates the file and cleans the data.
5. Find the cleaned file in the `Data/Output` folder.

## Output

Each cleaned file is saved separately using its original filename.

For example:

```text
employees_london.xlsx
```

will be saved as:

```text
employees_london_cleaned.xlsx
```

## Cleaning Report

After processing, the program displays a report containing:

- Original number of rows.
- Number of duplicate rows removed.
- Number of missing values found.
- Number of rows removed.
- Final number of rows.

## Author

GitHub: [@teter38e](https://github.com/teter38e)
