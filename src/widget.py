from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    masked_number = ""
    for symbols in account_card:
        if symbols.isalpha():
            masked_number += symbols + " "
        elif symbols.isdigit() and len(symbols) == 16:
            masked_number += get_mask_card_number(symbols)
        elif symbols.isdigit() and len(symbols) == 18:
            masked_number += get_mask_account(symbols)
    return masked_number