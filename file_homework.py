import requests
with open("poem_book.pdf", mode="bw") as hw_file:
    response = requests.get(" https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf")
    print(response.content)
    hw_file.write(response.content)

import json

with open("homework_file_1.json", mode="bw") as my_json_file:
    response_2 = requests.get("http://api.open-notify.org/astros.json")
    my_json_file.write(response_2.content)

    json.dumps(my_json_file, indent=4)

# to_string = json.dumps(my_json_file)
# from_string = json.loads(to_string)
#
# with open("homework_file_2.json") as json_file:
#     json.dump(my_json_file, json_file, indent=4)
#



