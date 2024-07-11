import csv
ukranian_airport = "UA"
with open("airport-codes_csv.csv", mode="r",) as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        if reader:
            row["iso_country"] = ukranian_airport
            total = row
            print(total)





