from unittest.mock import mock_open, patch

import pytest

from src.readers import get_data_from_csv, get_data_from_excel


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_data_from_csv_xlcx(mock_file):
    assert open("../data/test_csv.csv").read() == "data"
    mock_file.assert_called_with("../data/test_csv.csv")

    assert open("../data/test_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../data/test_excel.xlsx")
