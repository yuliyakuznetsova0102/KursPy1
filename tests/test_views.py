import pandas as pd
import pytest

from src.views import get_excel


def test_get_excel(get_excel_0):
    assert get_excel("dict")[360] == get_excel_0
    assert get_excel("dataframe").equals(pd.read_excel("../data/operations.xlsx"))
    with pytest.raises(ValueError):
        assert get_excel("Invalid format") == ValueError