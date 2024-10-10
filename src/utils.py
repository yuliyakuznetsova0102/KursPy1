import json
from datetime import datetime, time

import requests


def greetings_time():
    now = datetime.now()
    current_time = now.time()
    if current_time <= time(hour=12):
        greeting = "Доброе утро"
    elif current_time <= time(hour=18):
        greeting = "Добрый день"
    elif current_time <= time(hour=23):
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    response = {"greeting": greeting}
    return json.dumps(response, ensure_ascii=False)



def get_card_data(cards):
    response = []
    for card in cards:
        last_four_digits = card["number"][-4:]
        total_spent = sum(card["transactions"])
        cashback = total_spent // 100
        card_info = {"last_four_digits": last_four_digits, "total_spent": total_spent, "cashback": cashback}
    response.append(card_info)
    return json.dumps(response)



def get_top_transactions(transactions):
    sorted_transactions = sorted(transactions, key=lambda x: x["amount"], reverse=True)
    top_transactions = sorted_transactions[:5]
    response = {"top_transactions": top_transactions}
    return json.dumps(response)



def get_currency_rates(api_key):
    url = f"http://api.apilayer.com/exchangerates_data/latest?base=RUB&apikey={api_key}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data", "status_code": response.status_code}


api_key = "QlhUUzKgVejM1oCicQ7L5sGOemSZG0Mq"
currency_data = get_currency_rates(api_key)
print(json.dumps(currency_data, indent=4, ensure_ascii=False))


def get_sp500_stock_prices(api_key):
    url = "https://financialmodelingprep.com/api/v3/stock/list?apikey={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data, indent=4)
    else:
        return json.dumps({"error": "Unable to fetch data"}, indent=4)


api_key = "Xc8BdikXJ3heI6uTLia6S2vWYrqUYjsT"
sp500_data = get_sp500_stock_prices(api_key)
print(sp500_data)
