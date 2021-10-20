# Convert numbers to words
# Importing numbers from text file and making them into a dictionary
small_number_to_word_dict = {}
numbers_file = open("numbers.txt", "r")

for line in numbers_file:
    key, value = line.split()
    small_number_to_word_dict[key] = value

numbers_file.close()

# Creating list for big numbers
big_numbers = []

big_numbers_file = open("numbers2.txt", "r")

for line in big_numbers_file:
    x = []
    x.append(line.split(" "))
    a = str(x[0])
    b = a.lower()
    c = []
    c = b.split("\\")
    d = c[0]
    d = d[2:]
    big_numbers.append(d)

big_numbers_file.close()


def number_to_word(number_string="5525"):

    number_digits = len(number_string)
    number_list = []

    for number in number_string:
        number_list.append(number)

    if number_digits == 4:
        print(f"{small_number_to_word_dict['5']} {big_numbers[0]}", end=" ")
        number_list.pop(0)
        number_digits = len(number_list)

    if number_digits == 3:
        print(f"{small_number_to_word_dict['5']} {small_number_to_word_dict['100']}", end=" ")
        number_list.pop(0)
        number_digits = len(number_list)

    if number_digits == 2:
        print(f"{small_number_to_word_dict[str(number_list[0])]}{small_number_to_word_dict[str(number_list[1])]}")


    print()
    print(number_list)

#print(small_number_to_word_dict)
number_to_word()