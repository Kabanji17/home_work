import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [("7000792289606361", "7000 79** **** 6361"), ("7123793459606361", "7123 79** **** 6361")],
)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account, mask_account", [("73654108430135874305", "**4305"), ("73654108123424558560", "**8560")]
)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
