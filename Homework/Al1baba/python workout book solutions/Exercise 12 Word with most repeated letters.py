from collections import Counter
"""
Should have used sorted function here with a key to sort according to the values from counter/most_common methods
"""

def most_repeated_word(seq):
    most_common = Counter(seq[0]).most_common(1)  # Setting up the first word with most repeated letters
    final_word = seq[0]
    for word in seq:
        count = Counter(word).most_common(1)
        if count[0][1] > most_common[0][1]:         # Checking if the next word has more repeated letters
            most_common = count
            final_word = word
    return final_word


def most_repeated_vowels(word): # Returns most common vowel with amount
    count = Counter(word).most_common()
    vowels = "aeuio"
    for key, value in count:
        if key in vowels:
            return key, value


def most_repeated_vowels_in_word(seq):  # Goes through every word and returns one with the most vowels
    count = 0
    result = ""
    for word in seq:
        letter, value = most_repeated_vowels(word)
        if value > count:
            count = value
            result = word
    return result


words = ['this', 'is', 'an', 'elementary', 'test', 'example']
# print(most_repeated_word(words))

# print(most_repeated_vowels_in_word(words))













