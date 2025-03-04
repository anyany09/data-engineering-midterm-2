import pandas as pd

def generate_finance_data():
    finance_data = {
        "date": ["2025/03/01", "2025/03/02", "2025-03-03"],
        "Amount": [1234.567, None, 987.654],
        "Description": ["Payment", "Refund", "Purchase"]
    }
    df = pd.DataFrame(finance_data)
    df.to_csv("finance_data.csv", index=False)
    print("finance_data.csv generated.")

def generate_marketing_data():
    marketing_data = {
        "alt_name": ["Ad1", "Ad2", "Ad3"],
        "Clicks": [15.7, None, 25.2],
        "Impressions": [200, 150, 300]
    }
    df = pd.DataFrame(marketing_data)
    df.to_csv("marketing_data.csv", index=False)
    print("marketing_data.csv generated.")

def generate_scientific_data():
    scientific_data = {
        "date": ["03/01/2025", "03/02/2025", "03/03/2025"],
        "measurement": [0.1234567, None, 0.9876543],
        "experiment": ["ExpA", "ExpB", "ExpC"]
    }
    df = pd.DataFrame(scientific_data)
    df.to_csv("scientific_data.csv", index=False)
    print("scientific_data.csv generated.")

if __name__ == "__main__":
    generate_finance_data()
    generate_marketing_data()
    generate_scientific_data()
