def write_file(number_list):
    with open("valmiitalukuja.txt", "w+") as w:
        number_list = list(map(lambda x: round(x, 2), number_list))

        for number in number_list:
            w.write(f"{number}\n")


def read_file(file):
    number_count = 0

    with open(file) as f:
        number_list = [line[:-1] for line in f.readlines()]     # Taking all the numbers from the file to a list

        for numbers in number_list:     # Going through every number that is not dot
            for number in numbers:
                if number != ".":
                    number_count += 1

        number_list = list(map(lambda x: float(x), number_list))   # Making every string to float, so can use sum()
        total_sum = round(sum(number_list), 2)

        write_file(number_list)     # Calling the write_file function to write rounded numbers

        print(f"Lukujen summa oli {total_sum}.")
        print(f"Kaikkiaan numeromerkkejä oli {number_count}.")


def main():
    read_file("liukulukuja.txt")


if __name__ == '__main__':
    main()
