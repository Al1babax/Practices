import random


def write_file(file_name, value_list):
    number_list = []
    for _ in range(int(value_list[0])):
        rand_number = random.randint(int(value_list[1]), int(value_list[2]))
        number_list.append(rand_number)

    with open(file_name, "w+") as f:
        f.write(f"Arvottu {value_list[0]} lukua väliltä {value_list[1]}-{value_list[2]}.\n")
        for x in range(len(number_list)):
            f.write(f"{number_list[x]}\n")


def main():
    print("""Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä
ja kirjoittaa ne tekstitiedostoon.""")
    file_name = input("Anna tehtävän tiedoston nimi:  ")
    while True:
        values = input("Anna lukujen määrä, alaraja ja yläraja, esim. 7 1 37: ")
        values_list = values.split(" ")
        if values_list[0].isdigit() and values_list[1].isdigit() and values_list[2].isdigit():
            break
        else:
            print("Et antanut kolmea kokonaislukua, anna luvut uudestaan.")
    write_file(file_name, values_list)


if __name__ == '__main__':
    random.seed(1)
    main()
    print("Tiedosto 'tulokset.txt' luotu, kiitos ohjelman käytöstä.")
