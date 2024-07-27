from unittest.mock import patch

from src.external_api import get_sum_conversion_currency

transaction = {
    "id": 11111111,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "1.0", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 1111111111111111",
    "to": "Счет 11313131414141815161",
}

transaction_rub = {
    "id": 11111111,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "111111.11", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "MasterCard 1111111111111111",
    "to": "Счет 11313131414141815161",
}


@patch("requests.get")
def test_get_sum_conversion_currency_usd(mock_get):
    """Тест функции, когда валюта не в рублях"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1.0},
        "info": {"timestamp": 111111111, "rate": 30.0},
        "date": "2024-07-09",
        "result": 30.0,
    }
    assert get_sum_conversion_currency(transaction) == 30.0


@patch("requests.get")
def test_get_sum_conversion_currency_rub(mock_get):
    """Тест функции, когда валюта в рублях"""
    mock_get.return_value.json.return_value = {"amount": 111111.11}
    assert get_sum_conversion_currency(transaction_rub) == 111111.11
