def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    return f"{"*" * 2}{account_number[-4::]}"
