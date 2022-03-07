henkilötiedot = {}


def add_person():
    name = input("Henkilön nimi: ")
    hetu = input("Henkilötunnus: ")
    henkilötiedot[name] = hetu
    print(f"Henkilö {name} lisätty tietokantaan.")


def main():
    while True:
        run = input("Haluatteko lisätä uuden henkilön?(y/n): ")
        if run.lower() == "y":
            add_person()
            print()
        else:
            break
    print(list(henkilötiedot.values()))


if __name__ == '__main__':
    main()
