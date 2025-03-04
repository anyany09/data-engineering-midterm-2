import pandas as pd
from data_pipeline import process_pipeline

def main():
    # მონაცემების კითხულობა: შეგიძლიათ CSV ან JSON ფორმატი გამოიყენოთ.
    try:
        data = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("ფაილი 'data.csv' არ არის ნაჩვენები. გთხოვთ, უზრუნველყოთ მონაცემთა ფაილი.")
        return

    # მინიმალური მონაცემების ტიპის განსაზღვრა; აქ, მაგალითად, 'finance'
    source_type = 'finance'

    # დამუშავების პროცესის გაშვება
    processed_data = process_pipeline(data, source_type)

    # შედეგის დაბეჭდვა
    print("დამუშავებული მონაცემები:")
    print(processed_data.head())

if __name__ == '__main__':
    main()
