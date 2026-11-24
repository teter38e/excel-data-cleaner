# Excel Data Cleaner

A Python tool for cleaning and processing Excel files using Pandas.

## Features

- Read Excel files using Pandas
- Detect and remove duplicate rows
- Detect missing values
- Fill missing Age values with the average
- Fill missing City and Salary values with `"Unknown"`
- Generate a cleaning report
- Save cleaned data to a new Excel file

## Technologies

- Python
- Pandas
- OpenPyXL

## Project Structure

```text
excel-data-cleaner/
│
├── Data/
│   ├── Input/
│   │   └── sample_input.xlsx
│   └── Output/
│       └── cleaned_data.xlsx
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/teter38e/excel-data-cleaner.git
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

1. Place your Excel file in `Data/Input/`.
2. Run the program:

```bash
python main.py
```

3. Find the cleaned Excel file in `Data/Output/`.

## Cleaning Report

The program displays:

- Original number of rows
- Number of duplicate rows
- Number of missing values
- Number of removed rows
- Final number of rows

## Author

GitHub: https://github.com/teter38e