def vokaalit(s1: str):
    number_of_vowels = 0
    vowels_in_finnish = "aeiouyäö"

    for letter in s1:
        if letter in vowels_in_finnish:
            number_of_vowels += 1

    return number_of_vowels


print(vokaalit("Jukka meni bensa-asemalle tankkaamaan autoaan."))
