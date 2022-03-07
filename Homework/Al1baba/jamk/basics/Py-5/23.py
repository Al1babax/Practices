def ask_animals():
    return input("Name a animal you would like to add to the file?\n")


def write_file(l1, file_name):     # Writes animals into a text file
    with open(file_name, "w+") as f:
        for animal in l1:
            f.write(animal)
            f.write("\n")


def read_and_print_file(file_name):
    with open(file_name, "r") as f:
        file = f.readlines()
        file = [animal[:-1] for animal in file]     # Removing the \n new line from each line
        print(sorted(file))


def menu():
    print("""Animal program menu --> Select one of the following options
    1)Add animal
    2)Remove animal
    3)Print animals
    0)Stop the program
    """)


def main():
    animal_list = []
    file_name = "animals.txt"

    while True:     # programs main loop
        menu()
        decision = input("Your option: ")

        if decision == "1":
            new_animal = ask_animals()
            if new_animal.isalpha():  # Checks if the animal consists of letters
                animal_list.append(new_animal)
            else:
                print("Your animal was not valid, please try again.")
            print()

        elif decision == "2":
            print(f"Animal list: {animal_list}")
            remove_animal = input("which animal would you like to remove:\n")
            animal_list.remove(remove_animal)
            print()

        elif decision == "3":
            # Writes new animals to a file
            write_file(animal_list, file_name)
            # Reads and prints the animal file
            read_and_print_file(file_name)
            print()

        elif decision == "0":
            exit(0)
            break

        else:
            print("Your option was not valid, please try again.")
            print()


if __name__ == '__main__':
    main()
