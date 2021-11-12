def draw_menu():
    print("""Mitä haluat tehdä:
1) Testaa ValueError
2) Testaa IndexError
3) Testaa ZeroDivisionError
4) Testaa TypeError
0) Lopeta""")


def index_error():
    test_list = [11, 22, 33, 44, 55]
    index_decision = int(input("Anna indeksi 0-4: "))
    try:
        a = test_list[index_decision]
        print(f"Listan arvo on {a} indeksillä {index_decision}.")
    except IndexError:
        print(f"Tuli IndexError, indeksi {index_decision}.")


def zero_division_error():
    a = 4
    divider = int(input("Anna jakaja: "))
    try:
        result = a / divider
        print(f"{a}/{divider} on  {round(result, 2)}.")
    except ZeroDivisionError:
        print(f"Tuli ZeroDivisionError, jakaja {divider}.")


def type_error():
    value = input("Anna numero: ")
    try:
        value = value * value
    except TypeError:
        print("Tuli TypeError, itsellään kertominen ei onnistunut.")


def main():
    decision = 100
    draw_menu()
    while True:
        while True:
            try:
                decision = int(input("Valintasi: "))
                decision = str(decision)
                break
            except ValueError:
                print("Anna valinta kokonaislukuna.")

        if decision == "1":
            print("Valikko-ohjelma testaa ValueError'n.")
            try:
                decision = int(decision)
            except ValueError:
                print("Valintasi ei ole numero, yritä uudestaan.")
            draw_menu()
        elif decision == "2":
            index_error()
            draw_menu()
        elif decision == "3":
            zero_division_error()
            draw_menu()
        elif decision == "4":
            type_error()
            draw_menu()
        elif decision == "0":
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            draw_menu()


if __name__ == '__main__':
    main()
    print("Kiitos ohjelman käytöstä.")
