import pandas as pd
from transform_data import transform_data

def main():
    # მონაცემების ჩატვირთვა (CSV ფაილი)
    input_file = "data.csv"
    df = pd.read_csv(input_file)

    # ტრანსფორმაციის პარამეტრები
    column_mapping = {"old_col": "new_col"}
    date_format = "%Y-%m-%d"
    numeric_precision = 2
    missing_values = "fill_mean"
    filters = {"category": "A"}

    # მონაცემთა ტრანსფორმაცია
    transformed_df = transform_data(
        df,
        column_mapping=column_mapping,
        date_format=date_format,
        numeric_precision=numeric_precision,
        missing_values=missing_values,
        filters=filters
    )

    # შედეგის შენახვა
    output_file = "output.csv"
    transformed_df.to_csv(output_file, index=False)
    print(f"მონაცემები დამუშავდა და შენახულია {output_file} ფაილში.")

if __name__ == "__main__":
    main()
