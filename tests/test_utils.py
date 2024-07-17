import json
from unittest.mock import patch

from src.utils import get_transaction_info


def test_get_transaction_info():
    """Проверка работы функции с имитацией открытия JSON-файла"""
    mock_data = [
        {
            "id": 123,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 11872317823782",
            "to": "Счет 64686473672032589",
        }
    ]
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(mock_data)
        assert get_transaction_info("../data/operations.json") == [
            {
                "id": 123,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 11872317823782",
                "to": "Счет 64686473672032589",
            }
        ]


def test_get_transaction_info_invalid_file(capsys):
    """Проверка работы функции, когда указан несуществующий файл"""
    get_transaction_info(filename="../data/kakayato_hren.json")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_get_transaction_info_no_file(capsys):
    """Проверка работы функции, когда файла нет"""
    get_transaction_info(filename="")
    captured = capsys.readouterr()
    assert captured.out == ""
