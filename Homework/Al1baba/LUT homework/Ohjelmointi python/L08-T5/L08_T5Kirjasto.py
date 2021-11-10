class DecisionMenu:

    def __init__(self, menu_str_list: list, choice_numbers: int):
        self.menu_str_list = menu_str_list
        self.choice_numbers = choice_numbers

    def __str__(self):
        menu_list = []
        print_menu = "Mitä haluat tehdä:\n"
        for number in range(self.choice_numbers):
            menu_list.append([number + 1, self.menu_str_list[number]])

        for line in menu_list:
            print_menu += f"{line[0]}) {line[1]}\n"

        print_menu += f"0) Lopeta"

        return print_menu


def decision():
    choice = int(input("Valintasi: "))
    return choice


def read_file(file) -> list:
    with open(file) as f:
        total_lines = 0
        file_list = []

        for line in f.readlines():
            file_list.append(line[:-1])
            total_lines += 1

        print(f"Tiedosto '{file}' luettu, {total_lines} riviä.")

        return file_list


def analyze_data(file_list):
    result_value = 0
    # print(file_list)
    temp_value_list = list(map(lambda x1: x1.split(";"), file_list))
    # print(temp_value_list)
    result_list = []

    for x in range(len(temp_value_list)):
        for y in range(x + 1):
            result_value += int(temp_value_list[y][1])
        result_list.append(result_value)
        result_value = 0

    return result_list


def save_data(result_list):     # Mine does exactly what is asked in the exercise, but test output is wrong...
    with open("L08T5Tulos.txt", "w+") as w:
        result_list = list(map(lambda x: str(x), result_list))
        w.write(";".join(result_list) + ";\n")

        print("Tulokset tallennettu tiedostoon 'L08T5Tulos.txt'.")
