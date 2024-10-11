import logging
from datetime import datetime

import pandas as pd

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="report.log",
    filemode="w",
)
report_logger = logging.getLogger("report")


def log_results_to_file(file_name):
    """Декоратор для функций-отчетов, который записывает в файл результат,
    который возвращает функция, формирующая отчет."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, "a") as f:
                f.write(f"{datetime.now()}: {result}\n")
            return result

        return wrapper

    return decorator


def expenses_by_category(transactions, category, date=None):
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    if date is None:
        date = datetime.now()
        three_months_ago = date - pd.DateOffset(months=3)
        filtered_transactions = transactions[
            (transactions["category"] == category) & (transactions["date"] >= three_months_ago)
        ]
        total_expenses = filtered_transactions["amount"].sum()
        report_logger.info("Вывод трат по заданной категории за последние три месяца")
        return total_expenses
