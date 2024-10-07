from collections.abc import Callable
from datetime import datetime, timedelta

import pandas as pd


def log_results_to_file(file_name:str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, "w") as f:
                f.write(f"{datetime.now()}: {result}\n")
            return result

        return wrapper

    return decorator


@log_results_to_file('report.txt')
def spending_by_weekday(transactions, date=None):
    '''Функция принимает датафрейм с транзакциями и опциональную дату.
    Фильтрует транзакции за последние три месяца и вычисляет стредние траты по дням недели'''
    transactions["date"] = pd.to_datetime(transactions["date"])
    if date is None:
        date = datetime.now()
    three_months_ago = date - pd.DateOffset(months=3)
    recent_transactions = transactions[transactions["date"] >= three_months_ago]
    recent_transactions["weekday"] = recent_transactions["date"].dt.day_name()
    average_spending = recent_transactions.groupby("weekday")["amount"].mean()
    return average_spending.to_dict()
