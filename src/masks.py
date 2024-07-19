import logging


logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.info(f"Принимается на вход номер карты {card_number} и маскируется")
        mask_card_number = f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        return mask_card_number
    else:
        logger.error("Введенные данные некорректны")
        return ""


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if account_number.isdigit() and len(account_number) == 20:
        logger.info(f"Принимается на вход номер счета {account_number} и маскируется")
        mask_account = f"{"*" * 2}{account_number[-4::]}"
        return mask_account
    else:
        logger.error("Введенные данные некорректны")


if __name__ == "__main__":
    print(get_mask_card_number("1111111111111111"))
    print(get_mask_account("11111111111111111111"))
