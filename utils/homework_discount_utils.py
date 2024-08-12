
def get_cost_with_discount_from_cost(param_cost , param_discount ) -> float:
    if param_cost <= 0:
        raise ValueError("param_cost <= 0")
    if param_discount <= 0:
        raise ValueError("param_discount <= 0")
    if param_discount >= 100:
        raise ValueError("param_discount >= 100")
    result = param_cost / 100 * param_discount
    return float(result)


print(get_cost_with_discount_from_cost(100, 10))

