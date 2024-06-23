import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "account, mask_account",
    [("Счет 64686473678894779589", "Счет  **9589"), ("Счет 35383033474447895560", "Счет  **5560")],
)
def test_mask_account_card_for_account(account, mask_account):
    assert mask_account_card(account) == mask_account


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard  7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic  6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold  5999 41** **** 6353"),
    ],
)
def test_mask_account_card_for_card(card, mask_card):
    assert mask_account_card(card) == mask_card


@pytest.mark.parametrize(
    "data, new_data", [("2018-07-11T02:26:18.671407", "11.07.2018"), ("2019-12-31T02:26:18.671407", "31.12.2019")]
)
def test_get_data(data, new_data):
    assert get_data(data) == new_data
