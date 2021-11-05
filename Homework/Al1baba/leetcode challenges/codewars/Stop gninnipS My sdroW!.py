def spin_words(sentence):
    word_list = sentence.split(" ")
    for x, word in enumerate(word_list):
        if len(word) >= 5:
            word_list[x] = word[::-1]
    return " ".join(word_list)


print(spin_words("Hey fellow warriors"))
