import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(file_name="data.csv", num_rows=100):
    categories = ["A", "B", "C"]
    old_col_values = ["X", "Y", "Z", "W"]

    data = {
        "old_col": [random.choice(old_col_values) for _ in range(num_rows)],
        "category": [random.choice(categories) for _ in range(num_rows)],
        "value": [round(random.uniform(5, 50), 3) if random.random() > 0.1 else None for _ in range(num_rows)],
        "date": [(datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1500))).strftime("%Y-%m-%d") for _ in range(num_rows)]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print(f"Generated {num_rows} rows of data and saved to {file_name}")

if __name__ == "__main__":
    generate_data()