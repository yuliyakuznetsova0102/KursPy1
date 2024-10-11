import json
import logging
from datetime import datetime, time

import requests

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="utils.log",
    filemode="w",
)
utils_logger = logging.getLogger("utils")


def greetings_time():
    """Функция приветствия в формате "???", где ??? — «Доброе утро» / «Добрый день» /
    «Добрый вечер» / «Доброй ночи» в зависимости от текущего времени."""
    now = datetime.now()
    current_time = now.time()
    if current_time <= time(hour=12):
        greeting = "Доброе утро"
        utils_logger.info("Приветствие - Доброе утро")
    elif current_time <= time(hour=18):
        greeting = "Добрый день"
        utils_logger.info("Приветствие - Добрый день")
    elif current_time <= time(hour=23):
        greeting = "Добрый вечер"
        utils_logger.info("Приветствие - Добрый вечер")
    else:
        greeting = "Доброй ночи"
        utils_logger.info("Приветствие - Доброй ночи")
    response = {"greeting": greeting}
    return json.dumps(response, ensure_ascii=False)


def get_card_data(cards):
    """Функция, которая возвращает json ответ по каждой карте:последние 4 цифры карты; общая сумма расходов;
    кешбэк (1 рубль на каждые 100 рублей)."""
    response = []
    for card in cards:
        last_four_digits = card["number"][-4:]
        utils_logger.info("Последние 4 цифры карты")
        total_spent = sum(card["transactions"])
        utils_logger.info("Общая сумма расходов")
        cashback = total_spent // 100
        utils_logger.info("Кэшбек")
        card_info = {"last_four_digits": last_four_digits, "total_spent": total_spent, "cashback": cashback}
    response.append(card_info)
    utils_logger.info("Информация по карте")
    return json.dumps(response)


def get_top_transactions(transactions):
    """Функция, возвращающает json-ответ с топ-5 транзакций по сумме платежа."""
    sorted_transactions = sorted(transactions, key=lambda x: x["amount"], reverse=True)
    top_transactions = sorted_transactions[:5]
    response = {"top_transactions": top_transactions}
    utils_logger.info("Вывод Топ-5 транзакций")
    return json.dumps(response)


def get_currency_rates(api_key_1):
    """Функция, возвращающет json-ответ о курсе валют."""
    url = f"http://api.apilayer.com/exchangerates_data/latest?base=RUB&apikey={api_key_1}"
    headers = {"apikey": api_key_1}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        utils_logger.info("Вывод курса валют")
        return response.json()
    else:
        utils_logger.info("Ошибка вывода курса валют")
        return {"error": "Unable to fetch data", "status_code": response.status_code}


def get_sp500_stock_prices(api_key_2):
    """Функция, возвращающает json - ответ о стоимости акций из S&P500."""
    url = "https://financialmodelingprep.com/api/v3/stock/list?apikey={}".format(api_key_2)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        utils_logger.info("Вывод информации о стоимости акций S&P500")
        return json.dumps(data, indent=4)
    else:
        utils_logger.info("Ошибка вывода о стоимости")
        return json.dumps({"error": "Unable to fetch data"}, indent=4)
