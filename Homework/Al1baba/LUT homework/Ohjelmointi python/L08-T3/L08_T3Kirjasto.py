######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: 000679570
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
print("Käytetään lämpötilamuunnoskirjaston versiota 1.0")


def kelvin_celsius(kelvin):
    return kelvin - 273.15


def kelvin_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


def celsius_kelvin(celsius):
    return celsius + 273.15


def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def test():
    pass


if __name__ == '__main__':
    test()
