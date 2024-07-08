import json

data = {
    "name": "Alex",
    "available": False,
    "age": 15,
}

to_string = json.dumps(data)
# print(to_string)
from_string = json.loads(to_string, parse_float=str)
print(from_string)

with open("data.json", mode="w") as json_file:
    json.dump(data, json_file, indent=4)

with open("data.json", mode="w") as json_file:
    data2 = 







