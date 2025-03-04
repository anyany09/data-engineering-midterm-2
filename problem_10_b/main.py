#!/usr/bin/env python3
import pandas as pd
import numpy as np
from functools import partial
from datetime import datetime

# ============================
# ფინანსური პროცესორის ფუნქციები
# ============================

def standardize_columns(df):
    """სტანდარტიზაცია: სვეტების სახელების გარდაქმნა ქვედა რეგისტრში."""
    df = df.copy()
    df.columns = [col.strip().lower() for col in df.columns]
    return df

def convert_date_iso(df, date_col):
    """თარიღის გარდაქმნა ISO ფორმატში."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce').dt.date \
        .apply(lambda x: x.isoformat() if pd.notnull(x) else x)
    return df

def round_numbers(df, decimals):
    """რიცხვების დამრგვალება (გთხოვთ 2 ციფრისთვის)."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].round(decimals)
    return df

def fill_empty_with_zero(df):
    """ცარიელი უჯრედების შევსება ნულებით."""
    df = df.copy()
    return df.fillna(0)

def process_finance(df, date_col):
    df = standardize_columns(df)
    df = convert_date_iso(df, date_col)
    df = round_numbers(df, 2)
    df = fill_empty_with_zero(df)
    return df

# functools.partial-ის გამოყენებით დაფუძნებული პარამეტრი
finance_processor = partial(process_finance, date_col="date")


# ===============================
# მარკეტინგის პროცესორის ფუნქციები
# ===============================

def alternative_names_mapping(df, mapping):
    """ალტერნატიული სახელების რუქის გამოყენება სვეტების დასახელებისთვის."""
    df = df.copy()
    return df.rename(columns=mapping)

def remove_empty_values(df):
    """ცარიელი მნიშვნელობების მოცილება (რაიის მოღანება, სადაც აქვს NaN)."""
    df = df.copy()
    return df.dropna()

def round_numbers_whole(df):
    """რიცხვების დამრგვალება მთელ რიცხვამდე."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].round(0).astype(int)
    return df

def filter_positive_values(df):
    """მხოლოდ დადებითი რიცხვების ფილტრაცია (მხოლოდ მთელ რიცხვებს considers)."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    mask = (df[numeric_cols] > 0).all(axis=1)
    return df[mask]

def process_marketing(df, alt_names_map):
    df = alternative_names_mapping(df, alt_names_map)
    df = remove_empty_values(df)         # ძებნა: მოცილება NaN-ების
    df = round_numbers_whole(df)         # შემდეგ, რიცხვების დამრგვალება და int-ის კონვერტაცია
    df = filter_positive_values(df)
    return df

# დეფაულტური ალტერნატიული სახელების რუქა
default_alt_names_map = {
    "alt_name": "campaign_name",
    "Clicks": "clicks",
    "Impressions": "impressions"
}

marketing_processor = partial(process_marketing, alt_names_map=default_alt_names_map)


# ==============================
# სამეცნიერო პროცესორის ფუნქციები
# ==============================

def round_numbers_scientific(df, decimals):
    """რიცხვების დამრგვალება 4 ციფრამდე."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].round(decimals)
    return df

def fill_empty_with_mean(df):
    """ცარიელი უჯრედების შევსება სათოვრო საშუალო მნიშვნელობით."""
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        mean_val = df[col].mean()
        df[col].fillna(mean_val, inplace=True)
    return df

def save_date_timestamp(df, date_col):
    """თარიღის შენახვა timestamp ფორმატში."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce') \
        .apply(lambda x: x.timestamp() if pd.notnull(x) else x)
    return df

def process_scientific(df, date_col):
    df = round_numbers_scientific(df, 4)
    df = fill_empty_with_mean(df)
    df = save_date_timestamp(df, date_col)
    return df

scientific_processor = partial(process_scientific, date_col="date")


# ==============================
# მთავარი სკრიპტი
# ==============================

def main():
    # 1. ფინანსური მონაცემები
    print("=== ფინანსური მონაცემების პროცესირება ===")
    try:
        finance_df = pd.read_csv("finance_data.csv")
    except Exception as e:
        print("ფაილის გახსნის შეცდომა finance_data.csv-სთვის, გამოიყენება ნიმუშური მონაცემები:", e)
        finance_df = pd.DataFrame({
            "date": ["2025/03/01", "2025/03/02", "2025-03-03"],
            "Amount": [1234.567, None, 987.654],
            "Description": ["Payment", "Refund", "Purchase"]
        })
    processed_finance = finance_processor(finance_df)
    print(processed_finance)
    print("\n------------------------------\n")

    # 2. მარკეტინგული მონაცემები
    print("=== მარკეტინგული მონაცემების პროცესირება ===")
    try:
        marketing_df = pd.read_csv("marketing_data.csv")
    except Exception as e:
        print("ფაილის გახსნის შეცდომა marketing_data.csv-სთვის, გამოიყენება ნიმუშური მონაცემები:", e)
        marketing_df = pd.DataFrame({
            "alt_name": ["Ad1", "Ad2", "Ad3"],
            "Clicks": [15.7, None, 25.2],
            "Impressions": [200, 150, 300]
        })
    processed_marketing = marketing_processor(marketing_df)
    print(processed_marketing)
    print("\n------------------------------\n")

    # 3. სამეცნიერო მონაცემები
    print("=== სამეცნიერო მონაცემების პროცესირება ===")
    try:
        scientific_df = pd.read_csv("scientific_data.csv")
    except Exception as e:
        print("ფაილის გახსნის შეცდომა scientific_data.csv-სთვის, გამოიყენება ნიმუშური მონაცემები:", e)
        scientific_df = pd.DataFrame({
            "date": ["03/01/2025", "03/02/2025", "03/03/2025"],
            "measurement": [0.1234567, None, 0.9876543],
            "experiment": ["ExpA", "ExpB", "ExpC"]
        })
    processed_scientific = scientific_processor(scientific_df)
    print(processed_scientific)

if __name__ == "__main__":
    main()
