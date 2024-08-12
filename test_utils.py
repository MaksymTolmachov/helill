from random import random, randint

import pytest

from utils.math_utils import add_two_numbers

from utils.math_utils import get_two_time_string


def test_add_two_numbers():
    number1 = 2
    number2 = 3
    expected_result = 5.0
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected_result, "some strange 2+3!=5"


def test_add_two_numbers_zero():
    number1 = 0
    number2 = 0
    expected_result = 0.0
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected_result, "some strange 2+3!=5"


def test_add_two_numbers_minus():
    number1 = -10
    number2 = 9
    expected_result = -1
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected_result, "some strange 2+3!=5"


testing_args = [(2, 3, 5.0), (0, 0, 0.0), (-10, 9, -1)]


@pytest.mark.skip(reason="some strange behavior")
@pytest.mark.parametrize("number1, number2, expected_result", testing_args)
def test_add_two_numbers_combined(number1, number2, expected_result):
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == expected_result


def test_add_two_numbers_random():
    number1 = randint(1, 10**10)
    number2 = randint(1, 10**10)
    result = number1 + number2
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == result


testing_args_fail = [(50, 5, 55.0)]


@pytest.mark.parametrize("number1, number2, expected_result", testing_args_fail)
def test_add_two_numbers_raise_error(number1, number2, expected_result):
    with pytest.raises(ValueError):
        add_two_numbers(number1, number2)


def test_add_two_numbers_bla_random():
    number1 = randint(1, 10**10)
    number2 = randint(1, 10**10)
    result = number1 + number2
    actual_result = add_two_numbers(number1, number2)
    assert actual_result == result


class TestAddTwoNumbers:

    def test_add_two_numbers(self):
        number1 = 2
        number2 = 3
        expected_result = 5.0
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result, "some strange 2+3!=5"

    def test_add_two_numbers_zero(self):
        number1 = 0
        number2 = 0
        expected_result = 0.0
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result, "some strange 2+3!=5"

    def test_add_two_numbers_minus(self):
        number1 = -10
        number2 = 9
        expected_result = -1
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result, "some strange 2+3!=5"


def test_new_function():
    given = 6
    expected = "12"
    actual_result = get_two_time_string(number=given)
    assert actual_result == expected





