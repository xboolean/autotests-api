from typing import Any, Sized

from http import HTTPStatus


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


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f'Expected length: {len(expected)}. '
        f'Actual length: {len(actual)}'
    )