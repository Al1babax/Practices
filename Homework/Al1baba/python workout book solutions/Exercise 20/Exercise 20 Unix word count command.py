from typing import List, Any
from collections import Counter
"""
The challenge for this exercise is to write a wordcount function that mimics the wc
Unix command. 
Expected output(also the file we are working with):
This is a test file.

It contains 28 words and 20 different words.

It also contains 154 characters.

It also contains 11 lines.

It is also self-referential.

Wow!
"""


def wordcount(file):
    char_count = 0
    word_count = 0
    lines_count = 0

    with open("wcfile.txt") as p:
        for _ in p.readlines():
            lines_count += 1

    temp_data: list[Any] = list(filter(lambda x: False if x == "\n" else True, list(file)))  # Filters useless data
    # out and makes list
    for x in range(len(temp_data)):
        temp_data[x] = temp_data[x][:-1]  # Removes \n from lines
        char_count += sum(Counter(temp_data[x]).values())  # Counts all the characters and sum the values together
        word_count += len(temp_data[x].split())

    # each element in a list one line from the file, so I join everything to one string then split by whitespace
    # and use set to delete duplicates then use len to get the count
    unique_word_count = len(set((" ".join(temp_data)).split(" ")))

    print(f"""This is a test file.
It contains {word_count} words and {unique_word_count} different words.
It also contains {char_count} characters.
It also contains {lines_count} lines.
It is also self-referential.
Wow!
""")


with open("wcfile.txt") as f:
    wordcount(f)
