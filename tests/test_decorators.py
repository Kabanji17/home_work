import tempfile

import pytest

from src.decorators import log


def test_log():
    """Тестирует выполнение декорируемой функции"""

    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_success_consol(capsys):
    """Тестирует вывод лога об успешном выполнении в консоль"""

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_fail_consol(capsys):
    """Тестирует вывод лога об ошибке в консоль"""

    @log()
    def my_function(x, y):
        return x + y

    my_function("1", 2)
    captured = capsys.readouterr()
    assert "my_function error" in captured.out


def test_log_success_file(capsys):
    """Тестирует вывод лога об успешном выполнении в файл"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert "my_function ok" in logs


def test_log_fail_file(capsys):
    """Тестирует вывод лога об ошибке в файл"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y

    my_function("1", 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert "my_function error" in logs
