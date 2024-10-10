import json
from datetime import datetime

import pandas as pd

from src.utils import get_card_data, get_currency_rates, get_sp500_stock_prices, get_top_transactions, greetings_time


def read_excel_to_dict(file_path):
    df = pd.read_excel(file_path)
    records = df.to_dict(orient="records")
    return records


# Пример использования
file_path = "../data/operations.xlsx"
data = read_excel_to_dict(file_path)
print(data)


# Пример транзакций
transactions = [
    {"card_number": "1234567812345678", "amount": 250.0},
    {"card_number": "1234567812345678", "amount": 150.0},
    {"card_number": "8765432187654321", "amount": 300.0},
    {"card_number": "8765432187654321", "amount": 50.0},
    {"card_number": "1111222233334444", "amount": 100.0},
    {"card_number": "1111222233334444", "amount": 200.0},
]


cards_data = [
    {
        "card_number": "1234567812345678",
        "expenses": 1200,
        "transactions": [
            {"amount": 500, "description": "Покупка в магазине"},
            {"amount": 700, "description": "Оплата за услуги"},
            {"amount": 200, "description": "Перевод другу"},
            {"amount": 100, "description": "Кофе"},
            {"amount": 150, "description": "Обед"},
            {"amount": 50, "description": "Книги"},
        ],
    }
]


def main(date_time_str):
    current_datetime = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    response = {
        "greetings_time": greetings_time(current_datetime),
        "cards": get_card_data(cards_data),
        "top_transactions": [get_top_transactions(card) for card in cards_data],
        "currency_rates": get_currency_rates(),
        "sp500_stock_prices": get_sp500_stock_prices(),
    }

    return json.dumps(response, ensure_ascii=False, indent=4)


# Пример использования
date_time_input = "2023-10-01 14:30:00"
json_response = main(date_time_input)
print(json_response)
