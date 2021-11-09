######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

import math
import random


def circle_area(r):
    pi = math.pi
    return round(pi * pow(r, 2), 2)


def check_number(num1, secret_number):
    if num1 > secret_number:
        return 0
    elif num1 < secret_number:
        return 1
    else:
        return 2


def menu():
    print("""Mitä haluat tehdä:
1) Laskea ympyrän pinta-alan
2) Arvata luvun
0) Lopeta""")


def main():
    while True:
        menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            r = int(input("Anna ympyrän säde kokonaislukuna: "))
            value2 = circle_area(r)
            print(f"Säteellä {r} ympyrän pinta-ala on {value2}.")
            print()

        elif decision == 2:
            print("Arvaa ohjelman arpoma kokonaisluku.")
            random.seed(37)
            secret_number = random.randint(0, 1000)
            quess_counter = 1

            while True:
                num1 = int(input("Anna kokonaisluku välillä 0-1000: "))
                value = check_number(num1, secret_number)

                if value == 0:
                    print("Haettu luku on pienempi.")
                elif value == 1:
                    print("Haettu luku on suurempi.")
                elif value == 2:
                    print(f"Oikein! Käytit arvaamiseen {quess_counter} kierrosta.")
                    break

                quess_counter += 1
            print()

        elif decision == 0:
            break

        else:
            print("Väärä valinta, valitse uudestaan.")


if __name__ == '__main__':
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    main()
    print("Kiitos ohjelman käytöstä.")
