import lib


def draw_menu():
    print("""1) Anna tiedoston nimi
2) Lue tiedosto
3) Tulosta tiedosto
4) Kirjoita tiedosto
0) Lopeta""")


def main():
    file_name = ""
    file = None
    while True:
        draw_menu()
        decision = input("Anna valintasi: ")
        if decision == "1":
            file_name = input("Anna luettavan tiedoston nimi: ")
            # file_name = "L13T1_1.txt"
        elif decision == "2":
            if file_name != "":
                file = lib.File(file_name)
            else:
                print("Et ole vielä antanut tiedoston nimeä, valitse 1")
        elif decision == "3":
            if file_name == "":
                print("Et ole vielä antanut tiedoston nimeä, valitse 1")
            if file is None:
                print("Ohjelma ei ole vielä lukenut tiedostoa, valitse 2")
            if file_name != "" and file is not None:
                file.print_file()
        elif decision == "4":
            file.write_file()
        elif decision == "0":
            break
        else:
            print("Virhe valinta, valitse uudestaan")


if __name__ == '__main__':
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    main()
    print("Kiitos ohjelman käytöstä.")
