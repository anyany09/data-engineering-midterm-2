import pandas as pd

def transform_data(data, column_mapping=None, date_format=None,
                   numeric_precision=2, missing_values='drop',
                   filters=None):
    """
    მთავარი ფუნქცია მონაცემთა ტრანსფორმაციისთვის

    პარამეტრები:
    - data: დასამუშავებელი მონაცემები (DataFrame)
    - column_mapping: ლექსიკონი, რომელიც სვეტების სახელების გადარქმევას ახდენს
    - date_format: თარიღის ფორმატი გარდაქმნისთვის
    - numeric_precision: რიცხვების დამრგვალების სიზუსტე
    - missing_values: როგორ მოვიქცეთ ცარიელი მნიშვნელობებისას ('drop', 'fill_zero', 'fill_mean')
    - filters: გამოსაყენებელი ფილტრები (ლექსიკონი {column: value})

    აბრუნებს:
    - დამუშავებულ მონაცემებს
    """
    df = data.copy()

    # სვეტების გადარქმევა
    if column_mapping:
        df.rename(columns=column_mapping, inplace=True)

    # თარიღის ფორმატში გარდაქმნა
    if date_format:
        for col in df.select_dtypes(include=['datetime64', 'object']).columns:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime(date_format)
            except:
                pass

    # რიცხვების დამრგვალება
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].round(numeric_precision)

    # ცარიელი უჯრედების დამუშავება
    if missing_values == 'drop':
        df.dropna(inplace=True)
    elif missing_values == 'fill_zero':
        df.fillna(0, inplace=True)
    elif missing_values == 'fill_mean':
        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)

    # ფილტრები
    if filters:
        for col, value in filters.items():
            if col in df.columns:
                df = df[df[col] == value]

    return df
