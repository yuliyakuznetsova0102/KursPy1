import pytest
import pandas as pd

@pytest.fixture
def sample_transactions():
    data = {
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
        "amount": [100, 200, 150, 300, 250, 100, 50, 80, 90, 120],
    }
    return pd.DataFrame(data)