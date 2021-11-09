######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
import L08_T3Kirjasto


def draw_menu():
    print("""Minkä lämpötilamuunnoksen haluat tehdä?
1) Celsius->Fahrenheit
2) Celsius->Kelvin
3) Fahrenheit->Kelvin
4) Fahrenheit->Celsius
5) Kelvin->Celsius
6) Kelvin->Fahrenheit
0) Lopeta""")


def give_temp():
    return float(input("Anna lähtölämpötila: "))


def main():
    while True:
        draw_menu()
        decision = int(input("Valintasi: "))

        if decision == 1:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.celsius_fahrenheit(temp)
            print(f"Lämpötila Fahrenheit asteina: {round(new_temp, 2)}")
            print()

        elif decision == 2:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.celsius_kelvin(temp)
            print(f"Lämpötila Kelvin asteina: {round(new_temp, 2)}")
            print()

        elif decision == 3:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.fahrenheit_kelvin(temp)
            print(f"Lämpötila Kelvin asteina: {round(new_temp, 2)}")
            print()

        elif decision == 4:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.fahrenheit_celsius(temp)
            print(f"Lämpötila Celsius asteina: {round(new_temp, 2)}")
            print()

        elif decision == 5:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.kelvin_celsius(temp)
            print(f"Lämpötila Celsius asteina: {round(new_temp, 2)}")
            print()

        elif decision == 6:
            temp = give_temp()
            new_temp = L08_T3Kirjasto.kelvin_fahrenheit(temp)
            print(f"Lämpötila Fahrenheit asteina: {round(new_temp, 2)}")
            print()

        elif decision == 0:
            break

        else:
            print("Virheellinen valinta, valitse uudestaan.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
