"""
Making a translator that adds ub in front of every vowel  (a, e, i, o, or u)
"""


def ubbi_dubbi(str1):
    vowels = "aeuio"
    result = []

    for letter in str1:
        if letter in vowels.lower():
            result.append("ub" + letter)
        elif letter in vowels.upper():
            result.append("UB" + letter)
        else:
            result.append(letter)

    return "".join(result)


print(ubbi_dubbi("Elephant"))
print(ubbi_dubbi("Elephant") == "UBElubephubant")

















