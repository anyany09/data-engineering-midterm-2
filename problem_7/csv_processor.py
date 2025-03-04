import pandas as pd
import argparse

def process_csv(input_file, output_file, column_name, filter_value):
    # Read CSV file
    df = pd.read_csv(input_file)

    # Filter data based on the specified column and value
    filtered_df = df[df[column_name] == filter_value]

    # Save the processed data to a new CSV file
    filtered_df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a CSV file and save the output.")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument("output_file", help="Path to output CSV file")
    parser.add_argument("column_name", help="Column name to filter data")
    parser.add_argument("filter_value", help="Value to filter data by")

    args = parser.parse_args()

    # Run the CSV processing function
    process_csv(args.input_file, args.output_file, args.column_name, args.filter_value)