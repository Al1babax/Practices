def add_registration():
    new_number = input("Anna uusi auton rekisterinumero?(lopeta sammuttaa ohjelman): ")
    if new_number == "lopeta":
        return 0
    else:
        return new_number


def main():
    number = 1  # Setting initial number for the while loop to work
    registry = []

    while number != 0:
        number = add_registration()
        registry.append(number)

    registry.pop(-1)
    registry.sort()

    for item in registry:
        print(item)


if __name__ == '__main__':
    main()
