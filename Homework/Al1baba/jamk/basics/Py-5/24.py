def ask_number():
    return input("Write a number either whole number or decimal:\n")


def isfloat(num):
    num1 = num.split(".")

    if len(num1) == 2:
        try:
            float(num)
            return True
        except ValueError:
            return False


def isint(num):
    num1 = num.split(".")

    if len(num1) == 1:
        try:
            int(num)
            return True
        except ValueError:
            return False


def write_file(l1, filename):
    with open(filename, "w+") as f:
        for number in l1:
            f.write(number)
            f.write("\n")


def main():
    int_numbers = []
    float_numbers = []

    while True:
        current_number = ask_number()

        if isfloat(current_number):
            float_numbers.append(current_number)

        elif isint(current_number):
            int_numbers.append(current_number)
        else:
            break

    write_file(int_numbers, "int_numbers.txt")
    write_file(float_numbers, "float_numbers.txt")


if __name__ == '__main__':
    main()
