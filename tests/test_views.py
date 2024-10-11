import json
import unittest
from datetime import datetime
from unittest.mock import patch

import pandas as pd

from src.views import main, read_excel_to_dict


class TestReadExcelToDict(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_excel_to_dict(self, mock_read_excel):
        mock_data = {"Name": ["Alice", "Bob"], "Age": [25, 30], "City": ["New York", "Los Angeles"]}
        mock_df = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_df
        result = read_excel_to_dict("fake_path.xlsx")

        expected_result = [
            {"Name": "Alice", "Age": 25, "City": "New York"},
            {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        ]

        self.assertEqual(result, expected_result)

    @patch("pandas.read_excel")
    def test_empty_excel_file(self, mock_read_excel):

        mock_df = pd.DataFrame(columns=["Name", "Age", "City"])
        mock_read_excel.return_value = mock_df
        result = read_excel_to_dict("fake_path.xlsx")

        expected_result = []

        self.assertEqual(result, expected_result)

    @patch("pandas.read_excel")
    def test_incorrect_file_path(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError("File not found")
        with self.assertRaises(FileNotFoundError):
            read_excel_to_dict("incorrect_path.xlsx")


if __name__ == "__main__":
    unittest.main()


class TestMainFunction(unittest.TestCase):
    @patch("src.views.greetings_time")
    @patch("src.views.get_card_data")
    @patch("src.views.get_top_transactions")
    @patch("src.views.get_currency_rates")
    @patch("src.views.get_sp500_stock_prices")
    def test_main_function(
        self,
        mock_get_sp500_stock_prices,
        mock_get_currency_rates,
        mock_get_top_transactions,
        mock_get_card_data,
        mock_greetings_time,
    ):

        mock_greetings_time.return_value = "Добрый день"
        mock_get_card_data.return_value = [
            {"last_four_digits": "3456", "total_spent": 1500, "cashback": 15},
            {"last_four_digits": "7890", "total_spent": 2000, "cashback": 20},
        ]
        mock_get_top_transactions.return_value = {
            "top_transactions": [
                {"amount": 1000, "description": "Покупка 1"},
                {"amount": 500, "description": "Покупка 2"},
            ]
        }
        mock_get_currency_rates.return_value = {"USD": 75, "EUR": 85}
        mock_get_sp500_stock_prices.return_value = {"AAPL": 150, "GOOGL": 2800}

        date_time_str = "2023-10-01 14:30:00"
        cards = [
            {"number": "1234567890123456", "transactions": [1500]},
            {"number": "9876543210123456", "transactions": [2000]},
        ]
        transactions = [{"amount": 1000, "description": "Покупка 1"}, {"amount": 500, "description": "Покупка 2"}]
        api_key_1 = "QlhUUzKgVejM1oCicQ7L5sGOemSZG0Mq"
        api_key_2 = "Xc8BdikXJ3heI6uTLia6S2vWYrqUYjsT"

        result = main(date_time_str, cards, transactions, api_key_1, api_key_2)

        expected_response = {
            "greeting": "Добрый день",
            "card_info": [
                {"last_four_digits": "3456", "total_spent": 1500, "cashback": 15},
                {"last_four_digits": "7890", "total_spent": 2000, "cashback": 20},
            ],
            "top_transactions": {
                "top_transactions": [
                    {"amount": 1000, "description": "Покупка 1"},
                    {"amount": 500, "description": "Покупка 2"},
                ]
            },
            "currency_rates": {"USD": 75, "EUR": 85},
            "stock_prices": {"AAPL": 150, "GOOGL": 2800},
            "request_time": datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S").isoformat(),
        }
        self.assertEqual(json.loads(result), expected_response)


if __name__ == "__main__":
    unittest.main()
