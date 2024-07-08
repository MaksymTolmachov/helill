# my_file = open("main.py")
# print(my_file)
#
#
# print(my_file.read())
# print(my_file.closed)
# print(my_file.close)
# print(my_file.read())

import requests


def create_log(log: str, filename: str = "new_file.txt"):
    with open("new_file.txt", mode="a") as my_file:
        # print(my_file.read())
        my_file.write("\npoop")


create_log(log="kjkjlk")
create_log(log="kjkjlk")
create_log(log="kjkjlk")
create_log(log="kjkjlk")
create_log(log="kjkjlk")
create_log(log="kjkjlk")

def read_log(filename: str = "new_file.txt"):
    with open(filename, mode="r") as my_file:
        # logs = my_file.read()
        # print(logs.split())
        # my_file.seek(0)
        # data = my_file.readline()
        # print(data)


with open("git_presentation", mode="br") as my_file,





with open("", mode="br") as my_file:
    responce = requests.get()
    print(responce.content)





