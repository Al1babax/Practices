CAR_INFO = {
    "Car_1": ["Skoda", "ABC-123"],
    "Car_2": ["BMW", "ETC-235"],
    "Car_3": ["Renault", "OTS-963"],
    "Car_4": ["Opel", "RLC-274"],
    "Car_5": ["Skoda", "PEL-395"],
    "Car_6": ["Jeep", "KSY-385"],
    "Car_7": ["Mazda", "DPO-485"],
    "Car_8": ["Jaguar", "IFK-348"],
    "Car_9": ["Honda", "DIL-415"],
    "Car_10": ["Citroen", "APL-027"]
}


def main():
    car_brand = dict(sorted(CAR_INFO.items(), key=lambda item: item[1][0]))
    print(list(car_brand.values()))
    car_register = dict(sorted(CAR_INFO.items(), key=lambda item: item[1][1]))
    print(list(car_register.values()))


if __name__ == '__main__':
    main()
