import sys


def line_identity(file_list) -> dict:   # I should separate this function into two functions (check identity --> sort)
    file_identity_dict = {}
    for line in file_list:
        if line not in file_identity_dict:
            file_identity_dict[line] = 1
        else:
            file_identity_dict[line] += 1

    # file_identity_dict = dict(sorted(file_identity_dict.items()), key=lambda item: item[1])
    # Apparently the exercise wanted every result even if it only shows once
    """
    remove_list = []
    for key, value in file_identity_dict.items():
        if value <= 1:
            remove_list.append(key)

    for items in remove_list:
        file_identity_dict.pop(items)
    """
    # Sorting according to the keys on the dictionary which is auto alphabetically
    file_identity_dict = dict(sorted(file_identity_dict.items()), key=lambda item: item[0])
    file_identity_dict.pop("key")
    return file_identity_dict


def read_file(file_name) -> list:
    file_list = []
    try:
        with open(file_name) as f:
            for line in f.readlines():
                file_list.append(line[:-1])
    except FileNotFoundError:
        print(f"Tiedoston '{file_name}' avaaminen epäonnistui.")
        sys.exit()
    return file_list


def write_new_file(file_identity_dict):
    new_file_name = input("Anna kirjoitettavan tiedoston nimi: ")
    # new_file_name = "tulos.txt"
    with open(new_file_name, "w+") as f:
        for key, value in file_identity_dict.items():
            print(f"{key} {value}")
            f.write(f"{key} {value}\n")


def main():
    file_name = input("Anna luettavan tiedoston nimi: ")
    # file_name = "L10T2Data.txt"
    file_list = read_file(file_name)
    file_identity_dict = line_identity(file_list)
    # print(file_identity_dict)
    write_new_file(file_identity_dict)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
