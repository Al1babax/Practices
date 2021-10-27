from collections import Counter
"""
Iterating though each line of the text file and checking if a value separated by white lines is a digit -->
Adding all the digits together
"""

with open("asd.txt", "r") as f:
    temp_list = []
    result = 0

    for line in f:
        temp_list = line.split(" ")
        for value in temp_list:
            if value.isdigit():
                result += int(value)

    # print(result)

"""
Iterating through a file and if a line consist of 2 numbers multiply those and finally sum all the multiplied numbers
together.
"""
with open("numbers.txt") as w:
    temp_line = []
    result_numbers = []

    for line in w:
        temp_line = line.split()
        if temp_line[0].isdigit() and temp_line[1].isdigit():   # Checking if the line consist of 2 numbers
            number = int(temp_line[0]) * int(temp_line[1])
            result_numbers.append(number)

    final = sum(result_numbers)
    # print(final)


"""
Iterating through a file to count how many vowels there are
"""
VOWELS = "aeuio"
with open("numbers.txt") as file1:
    vowel_dict = {}
    temp_list2 = file1.read()
    c = dict(Counter(temp_list2))

    for key in c:
        if key in VOWELS:
            vowel_dict[key] = c[key]

    for key in sorted(vowel_dict):
        # print(f"{key}: {vowel_dict[key]}")
        pass
