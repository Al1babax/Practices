RAINFALL_DATA = {}


def get_rainfall():
    while True:
        city = input("Name of the city: ")

        if city == "":
            for city in RAINFALL_DATA:
                print(f"{city}: {RAINFALL_DATA[city]}")
            break

        amount = input("Quantity of rain in millimeters: ")
        RAINFALL_DATA[city] = amount


get_rainfall()











