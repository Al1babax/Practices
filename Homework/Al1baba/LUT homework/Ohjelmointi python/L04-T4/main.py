def divide_5_7(lower, upper):
    for _ in range(lower, upper + 1):
        if lower % 5 == 0:
            if lower % 7 == 0:
                print(f"Luku {lower} on jaollinen 5:llä ja 7:llä.")
                break
            else:
                print(f"{lower} ei ole jaollinen seitsemällä, hylätään.")
        else:
            print(f"{lower} ei ole jaollinen viidellä, hylätään.")
        lower += 1
    else:
        print("Alueelta ei löytynyt sopivaa arvoa.")
    print("Lopetetaan etsintä.")


def main():
    num1 = int(input("Anna alueen alaraja: "))
    num2 = int(input("Anna alueen yläraja: "))
    divide_5_7(num1, num2)


main()
