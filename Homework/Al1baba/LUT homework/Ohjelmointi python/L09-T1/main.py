import sys


def read_file(file, file_list) -> list:
    try:
        with open(file) as fr:
            print("Luetaan tiedosto ja suljetaan se.")
            line_count = 0

            for line in fr.readlines():
                file_list.append(line)
                line_count += 1

            print(f"Tiedoston '{file}' lukeminen onnistui, {line_count} riviä.")
            return file_list
    except IOError:
        print(f"Tiedoston '{file}' avaaminen epäonnistui.")
        sys.exit(0)


def write_file(file, file_list):
    try:
        with open(file, "w") as fw:
            print("Kirjoitetaan tiedosto ja suljetaan se.")

            for element in file_list:
                fw.write(element)

            print(f"Tiedoston '{file}' kirjoittaminen onnistui.")
    except IOError:
        print(f"Tiedoston '{file}' avaaminen epäonnistui.")
        sys.exit(0)


def main():
    file_list = []
    r_file = input("Anna luettavan tiedoston nimi: ")
    file_list = read_file(r_file, file_list)
    w_file = input("Anna kirjoitettavan tiedoston nimi: ")
    write_file(w_file, file_list)


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
