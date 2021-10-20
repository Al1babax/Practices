"""
Function for the default sum function, that takes any amount of numbers and then sum then -->
You can also choose a number as starting point for the function
"""


def my_sum(*args):
    asum = 0
    start_number = 0

    if isinstance(args[0], list):
        for number in range(len(args[0])):
            asum += args[0][number]
        try:
            start_number = args[1]
        except:
            pass

    if isinstance(args[0], tuple):
        for x in range(len(args[0])):
            asum += args[0][x]

    if not isinstance(args[0], list) and not isinstance(args[0], tuple):
        for x in range(len(args)):
            asum += args[x]

    return start_number + asum


def average_numbers(*args):
    digits = len(args)
    initial_sum = my_sum(args)
    return initial_sum / digits


def word_length(words=["Hi", "There", "j"]):
    word_dict = {}
    shortest_word = words[0]
    longest_word = ""
    sum_of_words_length = 0

    for word in range(len(words)):

        word_dict[words[word]] = len(words[word])

        if len(words[word]) > len(longest_word):
            longest_word = words[word]
        if len(words[word]) < len(shortest_word):
            shortest_word = words[word]

        sum_of_words_length += len(words[word])

    return f"Longest word was: {longest_word} and the shortest word was: {shortest_word}." \
           f"The average word length was: {round((sum_of_words_length / len(words)), 3)}"


def sum_everything_you_can(*args):
    items = len(args)
    number_list = []

    for x in range(items):
        try:
            a = int(args[x])
            number_list.append(a)
        except:
            "Cannot turn into a number"

    return my_sum(number_list)

#print(my_sum(1, 2, 3))
#print(my_sum([1, 2], 20))
#print(average_numbers(2, 5))
#print(word_length())

#print(sum_everything_you_can(2, 3, "cake", (15.2, 16), [1, 2]))

