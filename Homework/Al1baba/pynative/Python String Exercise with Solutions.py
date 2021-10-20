# 1A

str1 = "James"


# print(str1[::2])

# 1B

def middle_word(word):
    middle_index = int(len(word) / 2)
    print(word[middle_index - 1] + word[middle_index] + word[middle_index + 1])


str2 = "JhonDipPeta"
str3 = "JaSonAy"
# middle_word(str2)
# middle_word(str3)


# 2

s1 = "Ault"
s2 = "Kelly"


def word_inside_word(word1="a", word2="b"):
    return f"{word1[:2]}{word2}{word1[2:]}"
    pass


# print(word_inside_word(s1, s2))


# 3
sw1 = "America"
sw2 = "Japan"


def word_insert(word1="", word2=""):
    result = ""
    # for x in range(int((len(word1)) / 2)):

    result += f"{word1[0] + word2[0]}"
    result += f"{word1[int(len(word1) / 2)] + word2[int(len(word2) / 2)]}"
    result += f"{word1[-1] + word2[-1]}"

    return result


# print(word_insert(sw1, sw2))


# 4

stra1 = "PyNaTive"


def lower_char_first(word):
    temp = ""
    result = ""
    for letter in word:
        if letter.islower():
            result += letter
        else:
            temp += letter

    return result + temp


# print(lower_char_first(stra1))


# 5

strb1 = "P@#yn26at^&i5ve"


def count_symbols(word):
    chars, digits, symbols = 0, 0, 0

    for letter in word:
        if letter.isdigit():
            digits += 1
        elif letter.isalpha():
            chars += 1
        else:
            symbols += 1

    return chars, digits, symbols


# print(count_symbols(strb1))

# 6

s1 = "Abc"
s2 = "Xyz"


def mixed_string(s1, s2):
    result = ""
    for x in range(len(s1)):
        result += s1[x] + s2[-(x + 1)]
    return result


# print(mixed_string(s1, s2))

# 7

sa1 = "Yn"
sa2 = "PYnative"
sb1 = "Ynf"
sb2 = "PYnative"


def if_contains_string(s1, word):
    count = 0
    char_list = []
    [char_list.append(s1[x]) for x in range(len(s1))]

    for x in range(len(char_list)):
        if char_list[x] in word:
            count += 1

    return count == len(s1)


# print(if_contains_string(sa1, sa2))
# print(if_contains_string(sb1, sb2))


# 8

s8 = "Welcome to USA. usa awesome, isn't it?"


def find_usa(sentence):
    word = "usa"
    list1 = " ".split(sentence)
    count = 0

    for x in range(len(sentence)):
        if word == (sentence[x:x + 3]).lower():
            count += 1

    return count


# print(find_usa(s8))

# 9

str9 = "PYnative29@#8496"


def sum_num(str):
    sum1 = 0
    count = 0
    for symbol in str:
        if symbol.isdigit():
            sum1 += int(symbol)
            count += 1

    print(f"Sum is : {sum1} Average is {sum1 / count}")


# sum_num(str9)


# 10
# I need lot more practice with dictionaries, how to modify them specificly
str10 = "Apple"


def chars_in_string(str):
    char_dict = {}

    for letter in str:
        if letter not in char_dict:
            char_dict[letter] = 1

        elif letter in char_dict:
            a = char_dict.get(letter)
            a += 1
            char_dict[letter] = a

    print(char_dict)


# chars_in_string(str10)


# 11


str11 = "PYnative"


def reverse_string(str):
    a = []
    [a.append(str[x]) for x in range(len(str))]
    a.reverse()
    str2 = "".join(a)
    return str2


# print(reverse_string(str11))

# 12

str12 = "Emma is a data scientist who knows Python. Emma works at google."


def where_is_emma(str):
    for x in range(len(str)):
        # print(str[-x - 5:-x - 1]) # this line is just to see how the loop goes through every substring with lenght of 4 backwards and when it first encounters emma mark that index
        if str[-x - 5:-x - 1] == "Emma":
            return (-x - 5) + len(str12)

# print(where_is_emma(str12))


# 13

str13 = "Emma-is-a-data-scientist"

def split_string(str):
    str_list = str.split("-")
    [print(str_list[x]) for x in range(len(str_list))]

#split_string(str13)

#14

str_list14 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

def remove_empty(list):
    original_list = list.copy()
    new_list = list.copy()
    removed_count = 0

    for x in range(len(new_list)):
        if new_list[x - removed_count] == "" or new_list[x - removed_count] == None:
            new_list.pop(x - removed_count)
            removed_count += 1

    print(f"Original list of strings:\n{original_list}")
    print(f"After removing empty strings:\n{new_list}")



# remove_empty(str_list14)


# 15

str15 = "/*Jon is @developer & musician"

def remove_special_symbol(str):
    new_str = ""

    for symbol in str:
        if symbol.isalpha() or symbol == " ":
            new_str += symbol
    # After this we need to remove extra spaces, the hardest part of this exercise :D:D

    new_str_list = new_str.split(" ")

    count = 0
    for x in range(len(new_str_list)):
        if new_str_list[x - count] == "":
            new_str_list.pop(x - count)
            count += 1
    
    new_str = " ".join(new_str_list)

    print(new_str)

# remove_special_symbol(str15)

# 16


str16 = 'I am 25 years and 10 months old'

def remove_all_chars(str):
    result = ""

    for digit in str:
        if digit.isdigit():
            result += digit

    return int(result)



# print(remove_all_chars(str16))


# 17

str17 = "Emma25 is Data scientist50 and AI Expert"

def number_words(str):
    str_list = str.split(" ")
    numbers_in_words = []

    for word in range(len(str_list)):
        for symbol in range(len(str_list[word])):
            if str_list[word][symbol].isdigit() and str_list[word] not in numbers_in_words:
                numbers_in_words.append(str_list[word])

    [print(numbers_in_words[x]) for x in range(len(numbers_in_words))]

# number_words(str17)

# 18

str18 = '/*Jon is @developer & musician!!'

def replace_symbols(str):
    a = str
    for symbol in a:
        if not symbol.isdigit() and not symbol.isalpha() and symbol != " ":
            a = a.replace(symbol, "#")

    print(a)

# replace_symbols(str18)













