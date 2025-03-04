import pandas as pd
import numpy as np

def generate_sample_data(num_rows=100, output_file='data.csv'):
    # დაუცველი შემთხვევითი რიცხვების გენერაცია
    np.random.seed(42)

    # ფინანსური და მეცნიერული მონაცემებისათვის - შემთხვევითი რიცხვები
    revenue = np.random.randint(1000, 5000, size=num_rows)
    expense = np.random.randint(500, 3000, size=num_rows)
    measurement = np.random.normal(loc=50, scale=10, size=num_rows)

    # მარკეტინგული მონაცემებისათვის - არჩეული არხის (channel) მნიშვნელობები
    channels = np.random.choice(['online', 'retail', 'wholesale'], size=num_rows)

    # DataFrame-ის შექმნა
    df = pd.DataFrame({
        'revenue': revenue,
        'expense': expense,
        'measurement': measurement,
        'channel': channels
    })

    # DataFrame-ის CSV ფორმატში შენახვა
    df.to_csv(output_file, index=False)
    print(f"Sample data saved to {output_file}")

if __name__ == "__main__":
    generate_sample_data()
