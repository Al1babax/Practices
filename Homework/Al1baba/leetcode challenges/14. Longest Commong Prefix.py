def longest_common_prefix(strings: list[str]):
    letter_list = []
    count = 0
    if len(strings) == 0 or strings[0] == "":
        return ""

    for char_index in range(len(strings[0])):
        letter_list.clear()
        letter_list.append(strings[0][char_index])

        for word_index in range(len(strings)):
            try:
                if strings[word_index][char_index] not in letter_list[0]:
                    if count != 0:
                        return strings[0][:count]
                    else:
                        return ""
            except IndexError:
                return strings[0][:count]

        count += 1

    return strings[0][:count]


list1 = ["dog", "racecar", "car"]

print(longest_common_prefix(list1))

list2 = ["flower", "flow", "flight"]

print(longest_common_prefix(list2))

list3 = [""]
print(longest_common_prefix(list3))

print(longest_common_prefix(["flower", "flower", "flower", "flower"]))
