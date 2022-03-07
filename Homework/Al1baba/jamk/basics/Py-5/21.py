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


def main():
    animal_list = []
    file_name = "animals.txt"

    # This asks new animals
    while True:
        new_animal = ask_animals()
        if new_animal.isalpha():  # Checks if the animal consists of letters
            animal_list.append(new_animal)
        else:
            print("Your animal was not valid, please try again.")

        new_run = input("Would you like to add another animal? y/n\n")

        if new_run.lower() == "n":  # This stops the loop for asking new animals
            break

    # Writes new animals to a file
    write_file(animal_list, file_name)

    # Reads and prints the animal file
    read_and_print_file(file_name)


if __name__ == '__main__':
    main()
