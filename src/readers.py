import pandas as pd


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
    # print(get_data_from_csv("../data/transactions.csv"))
    print(get_data_from_excel("../data/transactions_excel.xlsx"))
