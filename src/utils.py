import json
import logging

import pandas as pd

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_transaction_info_from_json(filename: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(filename, "r", encoding="utf-8") as open_file:
            data_info = json.load(open_file)
            logger.info("Файл успешно открыт")
            if type(data_info) is not list:
                logger.error("Ошибка: TypeError")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Ошибка: {ex}")
        return []
    return data_info


def get_data_from_csv(csv_file: str) -> list[dict]:
    """Функция, которая принимает на вход путь до CSV-файла и преобразовывет его в список словарей"""
    df_csv = pd.read_csv(csv_file, delimiter=";")
    result = []
    for index, row in df_csv.iterrows():
        row_dict = {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {
                    "name": row["currency_name"],
                    "code": row["currency_code"],
                },
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        }
        result.append(row_dict)
    return result


def get_data_from_excel(excel_file: str) -> list[dict]:
    """Функция, которая принимает на вход путь до Excel-файла и преобразовывет его в список словарей"""
    df_excel = pd.read_excel(excel_file)
    result = []
    for index, row in df_excel.iterrows():
        row_dict = {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {
                    "name": row["currency_name"],
                    "code": row["currency_code"],
                },
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        }
        result.append(row_dict)
    return result


if __name__ == "__main__":
    # print(get_transaction_info_from_json(filename="../data/operations.json"))
    # print(get_data_from_csv("../data/transactions.csv"))
    print(get_data_from_excel("../data/transactions_excel.xlsx"))
