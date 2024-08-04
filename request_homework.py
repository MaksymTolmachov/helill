import requests
import pprint

url = "http://api.open-notify.org/astros.json"

response = requests.get(url=url)

response_json = response.json()
people = response_json["people"]


for person in people:
    print(person["name"])

print("---"*8)

# part two

url2 = "https://dummyjson.com/users"

response2 = requests.get(url=url2)

response_json2 = response2.json()
users = response_json2["users"]

for user in users:
    if user["age"] == 28:
        print(user["firstName"])






