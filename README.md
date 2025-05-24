# python-csv-cleaner
A simple Python script that automatically cleans messy CSV files by removing duplicates, fixing column names, and filling missing values.

#FEATURES

-Loads CSV files with automatic encoding detection (UTF-8, Latin-1)
-Skips malformed lines without crashing
-Removes duplicate rows
-Cleans column names by stripping whitespace and replacing spaces with underscores
-Fills missing values with a customizable default
-Trims whitespace from all text cells
-Automatically detects and standardizes date/time columns to YYYY-MM-DD format
-Validates and cleans numeric columns, converting strings with commas to numbers

#USAGE

from csv_cleaner import clean_csv  # if you put the function in csv_cleaner.py

cleaned_df = clean_csv("your_file.csv", fill_value="-")
print(cleaned_df)

#Or run the script directly:

Bash:
python csv_cleaner.py

Make sure to replace "your_file.csv" with the path to your CSV file

#REQUIREMENTS

-Python 3.x
-Pandas library

#WHY USE python-csv-cleaner

Messy CSV files are common in real-world data tasks. This script makes it easy to quickly clean and prep your data for analysis or further processing without headaches.
