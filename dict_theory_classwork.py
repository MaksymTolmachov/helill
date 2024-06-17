# from pprint import pprint
# person_name = "Alex"
# person_age = 16
#
# person = {
#     "name": "Alex",
#      "age": 16,
#      "hobbies": [
#          "soccer"
#          "tennis"
#      ],
#     "address": None,
# }
# address = person.get("address") or "Odesa"
# #address = person["address"]
# print(address)
# print(23 and 333)
#
# shipment = {}
# shipment["phone"] = "iPhoneX"
# shipment["plate"] = "from Ukraine with love"
# shipment["plate2"] = "from Ukraine with love34"
# shipment[5] = "toy"
# pprint(shipment, indent=1)
#
#
# item_from_shipment = shipment["phone"]
# item_from_shipment = shipment[5]
# item_from_shipment = shipment.get("5")
# item_from_shipment = shipment.get("5", "something")
#
# print(item_from_shipment)
#
#
#
# del shipment[5]
# shipment.pop("plate")
# shipment.pop("plate")

cars =[
    {
        "number": 1,
        "colour": "black",
        "price": 120.5,
        "features": [
            "jump"
            "radio"
            "retro"
        ]
    },
    {
        "number": 3,
        "colour": "black",
        "price": 56,
        "features": [],
        "in_sale": True,
        "empty": None
    },
    {
        "number": 12,
        "colour": "white",
        "price": 1200.5,
        "features": [
            "jump"
            "radio"
            "retro"
        ]
    },
]

# for car in cars:
#     print(f'price {car["price"]}')
#     for features in car.get("features", []):
#         print(features)
#     print("~" * 20)

my_tuple = 3, 77

person = {
    "name": "Alex",
     "age": 16,
     "hobbies": [
         "soccer"
         "tennis"
     ],
    "address": None,
}

for key in person.items():
    print(key)
    # print(person[item])
    print("~" * 20)


for key in person.items():
    print(key)
    # print(person[item])
    print("~" * 20)
