import pytest
from security import check_password_strength


def test_valid_passwords():
    assert check_password_strength("yigit123A*") is True
    assert check_password_strength("sdnoHHGB783!") is True


def test_missing_uppercase():
    assert check_password_strength("yigit123a*") is False
    assert check_password_strength("sdnosw783!") is False


def test_missing_digit():
    assert check_password_strength("yigitdswA*") is False
    assert check_password_strength("sdnoHHsaGB!") is False


def test_missing_special_char():
    assert check_password_strength("yigit123Aa") is False
    assert check_password_strength("sdnoHHGB783as") is False


def test_too_short():
    assert check_password_strength("yt13A*") is False
    assert check_password_strength("sB3!") is False


def test_exact_minimum_length():
    assert check_password_strength("yit123A*") is True
    assert check_password_strength("sdGB783!") is True
