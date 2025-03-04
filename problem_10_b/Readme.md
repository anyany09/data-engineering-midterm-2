# Data Processing Project

This project demonstrates how to create three specialized data processors for different datasets (finance, marketing, and scientific) using Python's `functools.partial`. The project includes sample CSV files for testing, along with scripts to run the main processing script on both Linux/Unix and Windows environments.

## Project Structure

- **main.py**  
  The main script that:
    - Reads sample CSV files.
    - Applies three specialized processors:
        - **finance_processor**:
            - Standardizes column names (converts them to lowercase).
            - Converts dates to ISO format.
            - Rounds numeric values to 2 decimal places.
            - Fills empty cells with zeros.
        - **marketing_processor**:
            - Renames columns using an alternative names mapping.
            - Removes rows with empty values.
            - Rounds numeric values to whole numbers (integer conversion).
            - Filters rows to include only those with positive numeric values.
        - **scientific_processor**:
            - Rounds numeric values to 4 decimal places.
            - Fills empty cells with the column’s mean value.
            - Converts date columns to timestamp format.
    - Prints the processed results.

- **generate_csv_samples.py** (Optional)  
  A helper script to generate the sample CSV files (`finance_data.csv`, `marketing_data.csv`, and `scientific_data.csv`).

- **run.sh**  
  A shell script for Linux/Unix systems to execute `script_linux.sh`.

- **run.bat**  
  A Windows batch script to run `script_windows.bat`.

- **commands.txt**  
  A file listing the command history used to run the project.

## Requirements

- Python
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

Install the required packages using pip:

```bash
pip install pandas numpy
