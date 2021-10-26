"""
Pig latin part 2
"""
from Exercise_5_Pig_latin import word_to_pig_latin


def pl_sentence(sentence="HELLOOO"):
    new_sentence_list = sentence.split(" ")
    final_sentence_list = []

    for word in new_sentence_list:
        final_sentence_list.append(word_to_pig_latin(word))

    final = " ".join(final_sentence_list)
    return final


# print(pl_sentence("this is a test translation"))


def make_secret_file(old_file, new_file):
    f = old_file.read()
    f_list = f.split(" ")
    for word in f_list:
        new_word = pl_sentence(word)
        new_file.write(new_word)
        new_file.write(" ")


def opening_files():
    with open("randomtext.txt", "r") as data, open("secrettext.txt", "w+") as data2:
        make_secret_file(data, data2)


# opening_files()        #This will translate the random.txt with Exercise 5 and 6 pig latin to secrettext.txt file





