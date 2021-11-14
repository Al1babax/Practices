import sys


def read_file(file_name):
    file_list = []
    try:
        with open(file_name) as f:
            for line in f.readlines():
                file_list.append(line[:-1])
        return file_list[1:]
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()


def check_file(file):
    new_file = []
    for x, line in enumerate(file):
        temp_list = line.split(";")
        if len(temp_list) == 3:
            if not temp_list[0].isdigit() or len(temp_list[0]) != 4:
                print(f"Virheellinen ID, rivillä {x + 2}: {line}")
            else:
                new_comment = check_comment(temp_list[1])
                new_points = check_points(temp_list[2])
                new_file.append(f"{temp_list[0]};{new_comment};{new_points}")
        elif len(temp_list) != 3:
            print(f"Väärä määrä arvoja, rivillä {x + 2}: {line}")

    return new_file


def check_points(points: str):
    try:
        points = int(points)
    except ValueError:
        points = 0
    return points


def check_comment(comment):
    new_comment = ""
    accepted_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    for symbol in comment:
        if symbol.upper() in accepted_alphabet or symbol.isdigit():
            new_comment += symbol
    return new_comment


def write_file(file):
    with open("siistitty.txt", "w+") as f:
        f.write("ID;Kommentti;Mainepisteet\n")
        for line in file:
            f.write(f"{line}\n")


def main():
    file_name = input("Anna luettavan tiedoston nimi: ")
    # file_name = "L12T3_1.txt"
    file = read_file(file_name)
    file = check_file(file)
    write_file(file)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
