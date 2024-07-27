from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict, None, None] | str:
    """Функция, принимает на вход список словарей, представляющих транзакции, возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    if not transactions_list or len(transactions_list) == 0:
        return "No transactions in such currency"
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formated_number = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formated_number
