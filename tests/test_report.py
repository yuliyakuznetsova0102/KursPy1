import unittest
from datetime import datetime, timedelta

import pandas as pd

from src.report import expenses_by_category, log_results_to_file


class TestExpensesByCategory(unittest.TestCase):

    def setUp(self):
        self.transactions = pd.DataFrame(
            {
                "date": [
                    datetime.now() - timedelta(days=30),
                    datetime.now() - timedelta(days=60),
                    datetime.now() - timedelta(days=120),
                    datetime.now() - timedelta(days=15),
                ],
                "category": ["food", "food", "transport", "food"],
                "amount": [100, 200, 300, 150],
            }
        )

    def test_expenses_by_category_with_no_matches(self):
        result = expenses_by_category(self.transactions, "transport")
        self.assertEqual(result, 0)


class TestLogResultsToFile(unittest.TestCase):

    def test_log_results_to_file(self):
        test_file = "test_log.txt"

        @log_results_to_file(test_file)
        def test_function(x):
            return x * 2

        open(test_file, "w").close()
        test_function(5)
        with open(test_file, "r") as f:
            log_content = f.read()
            self.assertIn("10", log_content)
            self.assertIn(datetime.now().strftime("%Y-%m-%d"), log_content)


if __name__ == "__main__":
    unittest.main()
