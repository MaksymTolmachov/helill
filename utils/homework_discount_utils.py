
def get_cost_with_discount_from_cost(param_cost , param_discount ) -> float:
    discount_for_counting = param_discount / 10
    result = param_cost * discount_for_counting
    return float(result)




