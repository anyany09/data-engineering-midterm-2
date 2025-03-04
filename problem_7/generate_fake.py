import pandas as pd

def generate_csv(filename="input.csv"):
    # Create sample data
    data = {
        "id": range(1, 11),
        "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"],
        "age": [25, 30, 35, 40, 22, 29, 33, 27, 31, 28],
        "category": ["sports", "music", "sports", "tech", "music", "tech", "sports", "tech", "music", "sports"]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV file
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' generated successfully.")

if __name__ == "__main__":
    generate_csv()