import requests
from pprint import pprint

url = "http://api.open-notify.org/astros.json"
response = requests.get(url=url)
response_json = response.json()
people = response_json["people"]


def get_name_people(people_names: list[dict], name: str) -> list[str]:
    content_list = []
    for person in people_names:

        pprint(person["name"])
        return content_list
