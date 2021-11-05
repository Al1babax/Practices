class Car:

    def __init__(self, brand, cost):
        self.cost = cost
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.cost}"


def menu():     # Luo menun
    print("""Käytettävissä olevat toiminnot:
1) Anna auton tiedot
2) Tulosta autojen tiedot
0) Lopeta""")


def print_list(list1):  # Printtaa jokasen auton tiedot
    for car in list1:
        print(car)


def main():
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    car_list = []

    while True:
        menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            car_brand = input("Anna auton merkki: ")
            car_cost = int(input("Anna auton hinta: "))
            auto = Car(car_brand, car_cost)
            car_list.append(auto)
            print()

        elif decision == 2:
            print("Listalta löytyy seuraavat automerkit ja hinnat:")
            print_list(car_list)
            print()

        elif decision == 0:
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()

    print("Kiitos ohjelman käytöstä.")


if __name__ == '__main__':
    main()










