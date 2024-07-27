import unittest
from collections import Counter

from src.searching import filter_transactions, search_transactions

example_transactions = [
    {"id": 1, "description": "Перевод организации", "amount": 1000},
    {"id": 2, "description": "Перевод с карты на карту", "amount": 200},
    {"id": 3, "description": "Оплата услуг", "amount": 300},
    {"id": 4, "description": "Перевод с карты на карту", "amount": 400},
    {"id": 5, "description": "Открытие вклада", "amount": 500},
    {"id": 6, "description": "Перевод со счета на счет", "amount": 600},
]


class TestTransactionFunctions(unittest.TestCase):

    def test_search_transactions(self):
        result = search_transactions(example_transactions, "Перевод организации")
        expected = [{"id": 1, "description": "Перевод организации", "amount": 1000}]
        self.assertEqual(result, expected)

        result = search_transactions(example_transactions, "Перевод с карты на карту")
        expected = [
            {"id": 2, "description": "Перевод с карты на карту", "amount": 200},
            {"id": 4, "description": "Перевод с карты на карту", "amount": 400},
        ]
        self.assertEqual(result, expected)

        result = search_transactions(example_transactions, "Не существующая операция")
        expected = []
        self.assertEqual(result, expected)

    def test_filter_transactions(self):
        categories_operations = [
            "Перевод организации",
            "Перевод с карты на карту",
            "Перевод с карты на счет",
            "Перевод со счета на счет",
            "Открытие вклада",
        ]
        result = filter_transactions(example_transactions, categories_operations)
        expected = {
            "Перевод организации": 1,
            "Перевод с карты на карту": 2,
            "Открытие вклада": 1,
            "Перевод со счета на счет": 1,
        }
        self.assertEqual(result, expected)

        result = filter_transactions(example_transactions, ["Оплата услуг"])
        expected = {"Оплата услуг": 1}
        self.assertEqual(result, expected)

        result = filter_transactions(example_transactions, ["Не существующая категория"])
        expected = {}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
