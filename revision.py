# # list
# from copy import copy, deepcopy
# from sys import getsizeof
#
# new_list = list()
# new_list2 = [3]
# new_list3 = ["string", 2, 3.0, True, False, None, new_list2]
# print(new_list3)
# print(id(new_list3))
# new_list3.append(444)
# print(id(new_list3))
#
# new_list2.append(555)
# print(new_list3)
#
# #do not use .append in "chikl" Ex. for something in something #
#
# for element in new_list3:
#     print(element)
#     new_list3.pop()
#
#
#
# new_iterator4 = iter(new_list3)
#
# print(next(new_iterator4))
# new_list3.append(55)
# new_list3.append(89)
#
# print(f"{getsizeof(new_list3)}")
#
#
# def foo(data: list = None):
#     if not data:
#         return []
#     data.append(2)
#     print(data)
#     return data
#
#
# n = 5
# m = n
# print(n)
# print(m)
#
# n = 7
#
# print(n)
# print(m)
#
# lst4 = new_list3
# lst4.append(7777777777)
# print(new_list3)
#
# print(11111111111)
# #for element in copy(new_list3):
# for element in deepcopy(new_list3):
#
#     print(element)
#     new_list2.append(67)
#     new_list3.pop()
#
#     print(new_list3)
#
# # lazy way of "COPY"
# #list_slice = new_list3[3:4]
# list_slice = new_list3[::2]
# new_list2.append("?????")
# print(list_slice)
# # print(new_list3)
#
#
# string = "i love balls"[::-1]


# set
# new_set = set()
# new_set1 = {}
# new_set2 = {3, 6, True, 77, [],}
#
# list_1 = [1, 2, 3, "fff"]
# set_from_list = set(list_1)
# set_from_string = set("I really love balls")
# print(set_from_list)
#
# for i in set_from_list:
#     print(i)


# my_tuple = (44)
# print(my_tuple)
# print(set1)
#
# print(type(set2))

set1 = {1, 2, 3}
set2 = {3, 4, 5}


# common element
comon1 = set1.intersection(set2)

print(f"{comon1=}")


# union element
all_elem1 = set1.union(set2)
print(f"{all_elem1=}")

# difference
diff = set1 - set2
print(f"{diff=}")

# all difference
total_diff = set1 ^ set2
print(f"{total_diff=}")

# dict
dict1 = {"name": "alex", "weight": 67}
dict2 = {"age": 13}

all_together = {**dict1, **dict2}
print(all_together)

dict1.update(dict2)








