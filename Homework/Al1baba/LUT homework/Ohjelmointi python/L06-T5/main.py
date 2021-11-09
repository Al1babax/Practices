"""
I read the question wrong, and though all cells are the steps, then thought there are 3 cells for steps....
Should read more carefully next time and not waste 30 mins :D:D
"""


def draw_menu():
    print("""Mitä haluat selvittää tiedostossa olevista askelmäärätiedoista:
1) Laske koko vuoden askelmäärä
2) Selvitä suurin päivittäinen askelmäärä
3) Tallenna yhteenvetotiedot
0) Lopeta""")


def write_new_file(total_steps, max_steps, new_file):
    with open(new_file, "w+") as w:
        w.write(f"Suurin päivittäinen askelmäärä oli {max_steps} askelta.\n")
        w.write(f"Ja koko vuoden askelmäärä oli {total_steps} askelta.\n")


def replace_comma_dot(str1):  # This is useless now...
    new_str = str1.split(",")
    return ".".join(new_str)


def yearly_steps(main_file):
    total_steps = 0
    max_steps_daily = 0

    with open(main_file) as f:

        for row in f.readlines():
            temp_list = row.split(";")
            temp_list = [temp_list[2]]

            # temp_list[2] = temp_list[2][:-1]

            for i in range(len(temp_list)):
                temp_list[i] = replace_comma_dot(temp_list[i])

            temp_list = list(map(lambda x: float(x), temp_list))
            total_steps += sum(temp_list)

            if max(temp_list) > max_steps_daily:
                max_steps_daily = max(temp_list)

    return int(round(total_steps, 0)), int(round(max_steps_daily, 0))


def main():
    main_file = input("Anna päivittäiset askeltiedot sisältävän tiedoston nimi: ")
    print("Tämä ohjelma laskee tunnuslukuja askeltietomääristä.")
    total_steps, max_steps = yearly_steps(main_file)
    # total_steps, max_steps = yearly_steps("2017Fitbit.txt")
    while True:
        draw_menu()
        decision = int(input("Valintasi: "))
        if decision == 1:
            print(f"Koko vuoden tulos oli {total_steps} askelta.")
            print()
        elif decision == 2:
            print(f"Suurin päivittäinen askelmäärä oli {max_steps} askelta.")
            print()
        elif decision == 3:
            write_file_name = input("Anna tulostieto-tiedoston nimi: ")
            write_new_file(total_steps, max_steps, write_file_name)
            print()
        elif decision == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            print()


if __name__ == '__main__':
    main()
