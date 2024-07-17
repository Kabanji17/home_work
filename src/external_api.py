import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_sum_conversion_currency(transaction: Any) -> Any:
    """Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return amount
        else:
            API_KEY = os.getenv("API_KEY")
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            data = response.json()
            return round(data["result"], 2)
    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        return 0.0
