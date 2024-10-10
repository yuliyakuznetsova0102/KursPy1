import os

import pandas as pd
import pytest
from conftest import sample_transactions

from src.report import average_spending_per_weekday


def test_average_spending_per_weekday(sample_transactions):
    result = average_spending_per_weekday(sample_transactions)
    assert set(result.keys()) == {"Sunday", "Monday", "Tuesday",
                                  "Wednesday", "Thursday",
                                  "Friday", "Saturday"}
    for value in result.values():
        assert isinstance(value, float)
    assert result["Monday"] == pytest.approx(200.0)
    assert result["Tuesday"] == pytest.approx(150.0)
    assert result["Wednesday"] == pytest.approx(300.0)


def test_log_results_to_file(sample_transactions):
    log_file = "report_results.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

    average_spending_per_weekday(sample_transactions)

    assert os.path.exists(log_file)
    with open(log_file, "r") as f:
        lines = f.readlines()
        assert len(lines) > 0
        assert "Monday" in lines[0]
    os.remove(log_file)


def test_average_spending_no_transactions():
    empty_transactions = pd.DataFrame(columns=["date", "amount"])
    result = average_spending_per_weekday(empty_transactions)
    assert result == {}


def test_average_spending_with_future_dates(sample_transactions):
    future_data = {
        "date": [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
            "2023-01-10",
            "2023-12-01",  # Будущая дата
        ],
        "amount": [100, 200, 150, 300, 250, 100, 50, 80, 90, 120, 400],
    }
    future_transactions = pd.DataFrame(future_data)
    result = average_spending_per_weekday(future_transactions)
    assert set(result.keys()) == {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
    assert "Monday" in result  # Убедимся, что понедельник по-прежнему присутствует
    assert result["Monday"] == pytest.approx(200.0)


def test_average_spending_with_varied_amounts(sample_transactions):
    varied_data = {
        "date": [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
            "2023-01-10",
        ],
        "amount": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    }
    varied_transactions = pd.DataFrame(varied_data)
    result = average_spending_per_weekday(varied_transactions)

    # Проверяем, что значения соответствуют ожиданиям
    assert result["Sunday"] == pytest.approx(75.0)  # Примерная проверка для воскресенья
    assert result["Monday"] == pytest.approx(20.0)  # Примерная проверка для понедельника
    assert result["Tuesday"] == pytest.approx(30.0)  # Примерная проверка для вторника


def test_average_spending_with_different_date_formats():
    varied_date_data = {
        "date": [
            "01/01/2023",
            "02/01/2023",
            "03/01/2023",
            "04/01/2023",
            "05/01/2023",
            "06/01/2023",
            "07/01/2023",
            "08/01/2023",
            "09/01/2023",
            "10/01/2023",
        ],
        "amount": [100, 200, 150, 300, 250, 100, 50, 80, 90, 120],
    }
    varied_date_transactions = pd.DataFrame(varied_date_data)
    varied_date_transactions["date"] = pd.to_datetime(varied_date_transactions["date"], format="%d/%m/%Y")
    result = average_spending_per_weekday(varied_date_transactions)
    assert set(result.keys()) == {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
