######################################################################
# CT10A0013 Ohjelmointi Pythonilla
# Tekijä: Sami Viik
# Opiskelijanumero: ########
# Päivämäärä: 09.11.2021
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: NaN
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

def print_berries(file):
    with open(file, "r") as f:
        line_number = 0
        for line in f.readlines():
            if line_number >= 1:
                temp_list = line.split(";")
                print(f"Kello oli {temp_list[2][:-1]}, kun punnittiin marjoja {temp_list[0]}.")
            line_number += 1


def main():
    main_file = "marjoja.txt"
    print_berries(main_file)


if __name__ == '__main__':
    main()
