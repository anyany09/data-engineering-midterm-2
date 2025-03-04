import pandas as pd
from functools import partial

def process_finance(data):
    """
    ფინანსური მონაცემების დამუშავება:
    - კვერთეულ მონაცემთა რიგისთვის დასახელებულია ჯამი ნომრებში.
    """
    numeric_cols = data.select_dtypes(include=['number']).columns
    data['finance_sum'] = data[numeric_cols].sum(axis=1)
    return data

def process_marketing(data):
    """
    მარკეტინგული მონაცემების დამუშავება:
    - კონვერტირებს არხის (channel) სახელს დიდ ასოებში, თუ არსებული სვეტი გვაქვს.
    """
    if 'channel' in data.columns:
        data['channel_upper'] = data['channel'].str.upper()
    return data

def process_scientific(data):
    """
    მეცნიერე მონაცემების დამუშავება:
    - ნორმალიზაცია: თითოეული ნომრიული სვეტის მნიშვნელობების ნორმალიზაცია.
    """
    numeric_cols = data.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        data[col + '_norm'] = (data[col] - data[col].mean()) / data[col].std()
    return data

def process_pipeline(data_source, source_type):
    """
    მონაცემთა კონვეიერი, რომელიც სხვადასხვა ტიპის მონაცემებს ამუშავებს.

    პარამეტრები:
    - data_source: მონაცემთა წყარო (DataFrame)
    - source_type: მონაცემების ტიპი ('finance', 'marketing', 'scientific')

    აბრუნებს:
    - დამუშავებულ მონაცემებს
    """
    # განსაზღვრეთ პროცესორის შესაბამისი ფუნქცია
    processor_map = {
        'finance': process_finance,
        'marketing': process_marketing,
        'scientific': process_scientific
    }

    if source_type not in processor_map:
        raise ValueError(f"Unknown source_type: {source_type}")

    # ჩვენ შეგვიძლია გამოყენოთ partial ფუნქცია, თუ გჭირდებათ დამატებითი პარამეტრები.
    processor = processor_map[source_type]
    return processor(data_source)
