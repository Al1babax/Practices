from random import randint

"""
I wrote this using OOP just for little practice. I tend to use it so little that always forget.
"""


class Lotto:
    def __init__(self):  # Initialize the lotto with 40 numbers
        self.numbers = [x + 1 for x in range(40)]
        self.winning_numbers = []

    def draw_number(self):  # Draw numbers with randint and then remove them from the pool of numbers
        numbers_left = len(self.numbers)
        number_index = randint(1, numbers_left) - 1
        number = self.numbers[number_index]
        self.numbers.pop(number_index)
        self.save_number(number)

    def save_number(self, num):  # Saves the number drawn to winning numbers
        self.winning_numbers.append(num)

    def current_winning_numbers(self):  # Shows the current winning numbers
        print(self.winning_numbers)

    def organize_numbers(self):  # Sorts the numbers to increasing order
        self.winning_numbers = sorted(self.winning_numbers)

    def write_file(self):   # Writes lotto numbers separated by comma to a text file called lotto.txt
        try:
            with open("lotto.txt", "w+") as f:
                lotto_numbers = self.winning_numbers
                lotto_numbers = [str(number) for number in lotto_numbers]
                lotto_numbers = ", ".join(lotto_numbers)
                f.writelines(lotto_numbers)
        except IOError:
            print("Something unexpected went wrong. Lotto numbers NOT saved successfully")


def main():
    lotto = Lotto()
    for _ in range(7):
        lotto.draw_number()
        lotto.current_winning_numbers()

    lotto.organize_numbers()
    print("These are the final numbers in order:")
    lotto.current_winning_numbers()
    lotto.write_file()


if __name__ == '__main__':
    main()
