"""
Exercise 6 part 1
Pig latin game will translate any word with the following rules:
If the word starts with a vowel it will add way to the end of the word
If the word starts with a consonant it will move the first letter to be the last and add ay to the word
"""


vowels = ["a", "e", "i", "o", "u"]

add1 = "way"

add2 = "ay"


def get_a_word():
    word = input("Input a word you'd like to translate into Exercise 6 pig latin: ")
    return word


def word_to_pig_latin(word):
    # word = "python"
    word_list = []
    word = word.lower()

    for x in range(len(word)):
        word_list.append(word[x])

    if word[0] == ".":
        word = word[1:]

    if word[0] in vowels:
        word = word + add1

    if word[0] not in vowels:
        word_list.append(word_list[0])
        word_list.pop(0)
        word_list.append(add2)
        word = "".join(word_list)

    return word


# TODO 1. Make a function and use string slicing or indexing not a list


def word_to_pig_latin2():
    pass


def play():
    running = True

    while running:
        word = get_a_word()
        print(word_to_pig_latin(word))
        still_going = (input("Would you like to translate another word?(y/n) ")).lower()

        if still_going == "n":
            running = False


if __name__ == "__main__":
    play()
