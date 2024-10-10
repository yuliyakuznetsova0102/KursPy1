import os
from datetime import datetime, timedelta

import pandas as pd


def log_results_to_file(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, "a") as f:
                f.write(f"{datetime.now()}: {result}\n")
            return result

        return wrapper

    return decorator


@log_results_to_file("report_results.txt")
def average_spending_per_weekday(transactions, date=None):
    transactions["date"] = pd.to_datetime(transactions["date"])
    if date is None:
        date = datetime.now()
    three_months_ago = date - pd.DateOffset(months=3)
    recent_transactions = transactions[transactions["date"] >= three_months_ago]
    recent_transactions["weekday"] = recent_transactions["date"].dt.day_name()
    average_spending = recent_transactions.groupby("weekday")["amount"].mean()
    return average_spending.to_dict()
