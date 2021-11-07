class Cars:

    def __init__(self, brand, count):
        self.brand = brand
        self.count = count

    def __str__(self):
        return f"Varastossa on nyt {self.brand}-merkkisiä autoja {self.count} kpl."


def create_car():
    brand = input("Anna automerkki: ")
    count = int(input("Anna automerkin lukumäärä varastossa: "))
    car = Cars(brand, count)
    return car


def main():
    auto = create_car()
    print(auto)


if __name__ == '__main__':
    main()















