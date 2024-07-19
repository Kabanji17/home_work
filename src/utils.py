import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_transaction_info(filename: str) -> list[dict]:
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


if __name__ == "__main__":
    print(get_transaction_info(filename="../data/operations.json"))
