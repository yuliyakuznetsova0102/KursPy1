import json
from datetime import datetime

import pandas as pd

from src.utils import get_card_data, get_currency_rates, get_sp500_stock_prices, get_top_transactions, greetings_time


def read_excel_to_dict(file_path):
    df = pd.read_excel(file_path)
    records = df.to_dict(orient="records")
    return records


def main(date_time_str, cards, transactions, api_key_1, api_key_2):
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    greeting = greetings_time()
    card_info = get_card_data(cards)
    top_transactions = get_top_transactions(transactions)
    currency_rates = get_currency_rates(api_key_1)
    stock_prices = get_sp500_stock_prices(api_key_2)

    response = {
        "greeting": greeting,
        "card_info": card_info,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
        "request_time": date_time.isoformat(),
    }

    return json.dumps(response, ensure_ascii=False)
