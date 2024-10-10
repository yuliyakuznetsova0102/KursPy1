import unittest
from unittest.mock import patch
from datetime import datetime
import json

from src.utils import greetings_time, get_card_data, get_top_transactions, get_currency_rates, get_sp500_stock_prices


class TestGreetingsTime(unittest.TestCase):

    @patch("datetime.datetime")
    def test_greeting_morning(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 1, 1, 9, 0, 0)  # 9:00 AM
        expected = json.dumps({"greeting": "Доброе утро"}, ensure_ascii=False)
        self.assertEqual(greetings_time(), expected)

    @patch("datetime.datetime")
    def test_greeting_afternoon(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 1, 1, 15, 0, 0)  # 3:00 PM
        expected = json.dumps({"greeting": "Добрый день"}, ensure_ascii=False)
        self.assertEqual(greetings_time(), expected)

    @patch("datetime.datetime")
    def test_greeting_evening(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 1, 1, 20, 0, 0)  # 8:00 PM
        expected = json.dumps({"greeting": "Добрый вечер"}, ensure_ascii=False)
        self.assertEqual(greetings_time(), expected)

    @patch("datetime.datetime")
    def test_greeting_night(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 1, 1, 23, 30, 0)  # 11:30 PM
        expected = json.dumps({"greeting": "Доброй ночи"}, ensure_ascii=False)
        self.assertEqual(greetings_time(), expected)


class TestGetCardData(unittest.TestCase):

    def test_single_card_no_transactions(self):
        cards = [{"number": "1234567890123456", "transactions": []}]
        expected = json.dumps([{"last_four_digits": "3456", "total_spent": 0, "cashback": 0}])
        self.assertEqual(get_card_data(cards), expected)

    def test_single_card_with_transactions(self):
        cards = [{"number": "1234567890123456", "transactions": [100, 200, 300]}]
        expected = json.dumps([{"last_four_digits": "3456", "total_spent": 600, "cashback": 6}])
        self.assertEqual(get_card_data(cards), expected)

    def test_card_with_large_transactions(self):
        cards = [{"number": "1111222233334444", "transactions": [10000, 20000, 30000]}]
        expected = json.dumps([{"last_four_digits": "4444", "total_spent": 60000, "cashback": 600}])
        self.assertEqual(get_card_data(cards), expected)


class TestGetTopTransactions(unittest.TestCase):

    def test_empty_transactions(self):
        transactions = []
        expected = json.dumps({"top_transactions": []})
        self.assertEqual(get_top_transactions(transactions), expected)

    def test_fewer_than_five_transactions(self):
        transactions = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}, {"id": 3, "amount": 50}]
        expected = json.dumps(
            {"top_transactions": [{"id": 2, "amount": 200}, {"id": 1, "amount": 100}, {"id": 3, "amount": 50}]}
        )
        self.assertEqual(get_top_transactions(transactions), expected)

    def test_exactly_five_transactions(self):
        transactions = [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
            {"id": 3, "amount": 50},
            {"id": 4, "amount": 300},
            {"id": 5, "amount": 150},
        ]
        expected = json.dumps(
            {
                "top_transactions": [
                    {"id": 4, "amount": 300},
                    {"id": 2, "amount": 200},
                    {"id": 5, "amount": 150},
                    {"id": 1, "amount": 100},
                    {"id": 3, "amount": 50},
                ]
            }
        )
        self.assertEqual(get_top_transactions(transactions), expected)


    def test_transactions_with_negative_amounts(self):
        transactions = [
            {"id": 1, "amount": -100},
            {"id": 2, "amount": 200},
            {"id": 3, "amount": 50},
            {"id": 4, "amount": -300},
            {"id": 5, "amount": 150},
        ]
        expected = json.dumps(
            {
                "top_transactions": [
                    {"id": 2, "amount": 200},
                    {"id": 5, "amount": 150},
                    {"id": 3, "amount": 50},
                    {"id": 1, "amount": -100},
                    {"id": 4, "amount": -300},
                ]
            }
        )
        self.assertEqual(get_top_transactions(transactions), expected)


if __name__ == "__main__":
    unittest.main()
