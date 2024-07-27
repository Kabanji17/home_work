from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import get_data_from_csv, get_data_from_excel
from src.searching import search_transactions
from src.utils import get_transaction_info_from_json
from src.widget import get_data, mask_account_card


def main() -> str:
    """функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    while choice not in ["1", "2", "3"]:
        print("Некорректный выбор. Попробуйте еще раз.")
        choice = input().strip()
    else:
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = "data/operations.json"
            result = get_transaction_info_from_json(file_path)
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_path = "data/transactions.csv"
            result = get_data_from_csv(file_path)
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_path = "data/transactions_excel.xlsx"
            result = get_data_from_excel(file_path)

    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()
        if status in statuses:
            print(f"Операции отфильтрованы по статусу {status}")
            break
        else:
            print(f"Статус операции {status} недоступен.")

    filtered_transactions = filter_by_state(result, status)

    print("Отсортировать операции по дате? Да/Нет")

    sort_choice = input().lower()

    while sort_choice not in ["да", "нет"]:
        print("Ввели некорректный символ. Попробуйте еще раз:")
        sort_choice = input("Отсортировать операции по дате? Да/Нет\n").lower()
    else:
        if sort_choice == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            order_choice = input().lower()
            while order_choice not in ["по убыванию", "по возрастанию"]:
                print("Ввели некорректный символ. Попробуйте еще раз:")
                order_choice = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            else:
                if order_choice == "по возрастанию":
                    filtered_transactions = sort_by_date(filtered_transactions, False)
                elif order_choice == "по убыванию":
                    filtered_transactions = sort_by_date(filtered_transactions)
        elif sort_choice == "нет":
            filtered_transactions = filtered_transactions

    print("Выводить только рублевые транзакции? Да/Нет")

    currency_choice = input().lower()

    while currency_choice not in ["да", "нет"]:
        print("Ввели некорректный символ. Попробуйте еще раз:")
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    else:
        if currency_choice == "да":
            filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        elif currency_choice == "нет":
            filtered_transactions = filtered_transactions

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    keyword_choice = input().lower()

    while keyword_choice not in ["да", "нет"]:
        print("Ввели некорректный символ. Попробуйте еще раз:")
        keyword_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    else:
        if keyword_choice == "да":
            keyword = input("Введите слово для поиска:\n")
            filtered_transactions = search_transactions(filtered_transactions, keyword)
        elif keyword_choice == "нет":
            filtered_transactions = filtered_transactions

    print("Распечатываю итоговый список транзакций...")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            date = get_data(transaction["date"])
            description = transaction["description"]
            from_ = mask_account_card(transaction.get("from", ""))
            to_ = mask_account_card(transaction.get("to", ""))
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]

            print(f"{date} {description}\n{from_} -> {to_}\nСумма:{amount} {currency}\n")

    return "well done"


if __name__ == "__main__":
    main()
