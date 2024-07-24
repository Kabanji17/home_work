import re
from collections import Counter
from src.utils import get_transaction_info_from_json


list_transactions = get_transaction_info_from_json("../data/operations.json")

def search_transactions(data_transactions: list[dict], searching_string: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка."""
    searching_list = []
    for transaction in data_transactions:
        if "description" in transaction and re.findall(searching_string, transaction["description"]):
            searching_list.append(transaction)
    return searching_list


def filter_transactions(data_trasactions: list[dict], list_of_categories: list) -> dict:
    """Функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    searching_list = []
    for transaction in data_trasactions:
        if "description" in transaction and transaction["description"] in list_of_categories:
            searching_list.append(transaction["description"])
    return dict(Counter(searching_list))



if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]
    print(search_transactions(list_transactions, "Перевод организации"))
    print(filter_transactions(list_transactions, categories_operations))