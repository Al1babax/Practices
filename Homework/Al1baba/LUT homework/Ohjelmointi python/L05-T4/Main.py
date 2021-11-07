def check_str(str1: str) -> int:
    char_count = 0
    for _ in str1:
        char_count += 1
    return char_count


def ask_str():
    str1 = input("Anna merkkijono, 5-15 merkkiä: ")

    return str1


def main():
    while True:
        str1 = ask_str()
        char_count = check_str(str1)
        if 5 <= char_count <= 15:
            print(f"Annoit sopivan merkkijonon, {char_count} merkkiä.")
            break
        elif char_count < 5:
            print(f"Liian lyhyt, {char_count} merkkiä, anna uusi.")
        else:
            print(f"Liian pitkä, {char_count} merkkiä, anna uusi.")


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
