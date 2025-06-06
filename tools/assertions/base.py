from http import HTTPStatus
from typing import Any


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_equal(actual, expected, message=None):
    """
    Проверяет, что два значения равны.
    
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    """
    assert actual == expected, message or f"Expected {expected}, but got {actual}"


def assert_status_code(actual: Any, httpx_code: HTTPStatus):
    assert actual == httpx_code
