import pytest

from utils.homework_discount_utils import get_cost_with_discount_from_cost


testing_args = [(0, 10, 0), (200, 110, -20), (200, -20, 220)]


@pytest.mark.parametrize("param_cost, param_discount, expected_result", testing_args)
def test_cost_with_discount_from_cost_testing(param_cost, param_discount, expected_result):
    actual_result = get_cost_with_discount_from_cost(param_cost, param_discount)
    assert actual_result == expected_result





