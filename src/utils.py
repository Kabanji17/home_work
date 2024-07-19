import json


def get_transaction_info(filename: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(filename, "r", encoding="utf-8") as open_file:
            data_info = json.load(open_file)
            if type(data_info) is not list:
                return []
    except FileNotFoundError:
        return []
    return data_info
