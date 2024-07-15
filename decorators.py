from typing import Callable



def add_two_numbers(n_1: int, n_2: int) -> int:
    result = n_1 + n_2
    return result
#
#
# # print(foo)
# # print(type(foo))
# # print(type(55))
# # print(type(55.5))
# # print(foo.__code__)
# # print(foo.__dict__)
# # foo.age = 55
# # print(foo.__dict__)
#
# # new_func = foo
# # print(new_func)
# # print(foo)
# # n = print
# # n(787890)
#
# def wrapper(func: Callable, *args, **kwargs):
#     result = func(*args, **kwargs)
#     return result
#
# result = wrapper(add_two_numbers,number_two=88, number_one=77)
#  print(result)





# add_two_numbers(number_two=88, number_one=77)


d = 999


def simple_decorator(func: Callable):
    def wrapper(*args, **kwargs):
       # print("before")
       result = func(*args, **kwargs)
       with open("log.csv", mode="a", encoding="utf-8") as log_file:
           log_file.write(f"{func.__name__};{result};{args};{kwargs}\n")



       return result
    wrapper.__name__ = func.__name__
    return wrapper

# add_two_numbers = simple_decorator(func=add_two_numbers)
# print(add_two_numbers)
# # res = add_two_numbers(55, 888)
# # print(add_two_numbers)
# # print(res)
#
# res = add_two_numbers(4, 5)
# print(res)
#























