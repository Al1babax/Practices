# (c) LUT 2019 L11_T3.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
###########################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: 
# Opiskelijanumero: 
# Päivämäärä:
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
# Ohjelma, joka etsii sopivia numeroita

import time
import sys


def hakufunktio():
    luvut = ["", ""]
    luvut[0] = 0  # Pienempi luku tallennetaan tähän
    luvut[1] = 0  # Suurempi luku tallennetaan tähän


# Lisättävä koodi alkaa alta.
    file_name = input("Anna tiedoston nimi: ")
    file_list = []
    try:
        with open(file_name) as f:
            for line in f.readlines():
                file_list.append(line[:-1])
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()
    file_list.sort()
    """
    for x in range(len(file_list)):
        if min(luvut) < luvut[x + 1]:
            return [min(luvut), luvut[x + 1]]
    return [0, 0]
    """
    if int(file_list[0]) < int(file_list[-1]) / 3:
        return [int(file_list[0]), int(file_list[-1])]
    else:
        return [0, 0]
# Lisättävä koodi loppuu ylle.  


def paaohjelma():
    kello1 = time.perf_counter()
    tulosluvut = hakufunktio()
    kello2 = time.perf_counter()
    aika = kello2 - kello1
    if ((tulosluvut[0] == 0) and (tulosluvut[1] == 0)):
        print("Hakualgoritmisi ei löytänyt sopivaa lukuparia.")
    elif (aika > 2):
        print("Hakualgoritmisi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmisi oli riittävän nopea!")
        print("Se löysi sopivan parin:", tulosluvut[0], "ja", tulosluvut[1])
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

###########################################################################
# eof
