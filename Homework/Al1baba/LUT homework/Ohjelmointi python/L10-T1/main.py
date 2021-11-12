import sys


def reformat_lines(data):
    new_file = input("Anna kirjoitettavan tiedoston nimi: ")
    # new_file = "tulos.txt"
    line_count = 0

    with open(new_file, "w+") as f:
        for line in data:
            f.write(f"{line.lower()}\n")
            line_count += 1

    print(f"Kirjoitettiin {line_count} riviä tiedostoon '{new_file}'.")


def read_and_validate_file():
    file_name = input("Anna luettavan tiedoston nimi: ")
    # file_name = "L10T1Data.txt"
    total_lines_count = 1
    removed_lines = 1
    filtered_data_lines = []

    try:
        with open(file_name) as f:
            for line in f.readlines():
                if any(char.isdigit() for char in line):
                    removed_lines += 1
                else:
                    filtered_data_lines.append(line[:-1])
                total_lines_count += 1
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()

    print(f"Luettiin {total_lines_count} riviä tiedostosta '{file_name}'.")
    print(f"Hylättiin {removed_lines} riviä.")
    return filtered_data_lines


def main():
    new_data = read_and_validate_file()
    reformat_lines(new_data)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
