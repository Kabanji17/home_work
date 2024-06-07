import re

from .masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    name_card = ""
    masked_number = ""
    masked_card_number = ""
    for symbol in account_card:
        if symbol.isalpha():
            name_card += symbol
        elif symbol.isalpha() and bool(re.search("[а-яА-я]", symbol)):
            name_card += symbol
        elif symbol.isdigit():
            masked_number += symbol
    if len(masked_number) == 16:
        masked_card_number = name_card + " " + get_mask_card_number(masked_number)
    elif len(masked_number) == 20:
        masked_card_number = name_card + " " + get_mask_account(masked_number)
    return masked_card_number


def get_data(data: str) -> str:
    """Функция преобразования даты формата ГГГГ-ММ-ДД в формат ДД-ММ-ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
