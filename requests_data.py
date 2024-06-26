import requests
from pprint import pprint
url = "https://dummyjson.com/todos?imit=50skip=5"

response = requests.get(url=url)

params = {
    "limit": 300,
    "skip": 0
}

# print(response)
# # print(response.content)
# # print(response.text)
# # pprint(response.json(), indent=4, width=30)

# completed_todos = 0
# for todo in todos:
#     if todo["completed"]:
#         completed_todos += 1
#
# print(completed_todos)


import requests
from pprint import pprint


url = 'https://dummyjson.com/todos'

# response = requests.get(url=url, params=params)
#
# # print(response)
# # print(response.content)
# # print(response.text)
# response_json = response.json()
# todos = response_json['todos']


def get_todos(limit: int = 50, start: int = 0) -> list[dict]:
    params = {
        'limit': limit,
        'skip': start,
    }
    response = requests.get(url=url, params=params)
    response_json = response.json()
    todos = response_json['todos']
    return todos

def get_completed_todos_number(todos_candidates: list[dict], is_completed: bool = True) -> int:
    counter = 0
    for todo in todos_candidates:

        if todo['completed'] is is_completed:
            counter += 1
    return counter


start = 0
limit = 50
has_next = True
for iterator in range(1, 301):
    chunk = get_todos(start=start, limit=limit)
    start += limit
    print(chunk)


