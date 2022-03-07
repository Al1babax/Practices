def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            name_list = f.readlines()
            name_list = [name[:-1] for name in name_list]
            return name_list
    except FileNotFoundError:
        print("File nimet.txt does not exist.")
        return []


def count_names(name_list):     # Counts the names and sort according to the highest appearance
    name_dict = {}
    for name in name_list:
        if name not in name_dict:
            name_dict[name] = 1
        else:
            name_dict[name] += 1
    return dict(sorted(name_dict.items(), key=lambda nimi: nimi[1], reverse=True))


def main():
    name_list = read_file("nimet.txt")
    if len(name_list) >= 1:
        print(count_names(name_list))


if __name__ == '__main__':
    main()
