from .masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    masked_number = ""
    for symbol in account_card:
        if symbol.isalpha():
            masked_number += symbol
    for symbol in account_card:
        if symbol.isdigit() and len(symbol) == 16:
            masked_number += get_mask_card_number(symbol)
        elif symbol.isdigit() and len(symbol) == 18:
            masked_number += get_mask_account(symbol)
    return masked_number


def get_data(data: str) -> str:
    """Функция преобразования даты формата ГГГГ-ММ-ДД в формат ДД-ММ-ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
