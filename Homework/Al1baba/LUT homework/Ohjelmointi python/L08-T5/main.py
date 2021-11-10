import L08_T5Kirjasto as kj


def main():
    file_list = []
    result_list = []

    while True:
        new_menu = kj.DecisionMenu(["Lue tiedosto", "Analysoi tiedot", "Tallenna tulokset"], 3)
        print(new_menu)
        choice = kj.decision()

        if choice == 1:
            file = "L08T5Data.txt"
            file_list = kj.read_file(file)
            print()

        elif choice == 2:
            result_list = kj.analyze_data(file_list)
            print(f"Tiedot analysoitu, arvot yhteensä {sum(result_list)}.")
            print()

        elif choice == 3:
            kj.save_data(result_list)
            print()

        elif choice == 0:
            break

        else:
            print("Väärä valinta, valitse uudestaan.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
