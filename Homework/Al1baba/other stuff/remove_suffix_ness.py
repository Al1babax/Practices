"""
parameter word: str of word to remove suffix from.
return: str of word with suffix removed & spelling adjusted.

This function takes in a word and returns the base word with `ness` removed.
However with spelling rules: If the root word originally ended in a consonant followed
by a 'y', then the 'y' was changed to to 'i'. Removing 'ness' needs to restore the
'y' in those root words
examples:
remove_suffix_ness('wellness') -> 'well'
remove_suffix_ness('sadness') -> 'sad'
remove_suffix_ness('ridiculousness') -> 'ridiculous'
remove_suffix_ness('ordinariness') -> 'ordinary'
remove_suffix_ness('heaviness') -> 'heavy'
you can just ignore and remove all the comments when you submit homework
assumption is that the word is a legit english word
"""


def remove_suffix_ness(word: str) -> str:
    try:
        if "ness" in word:
            word = word.replace("ness", "")

            if word[-1] == "i":
                word = word.replace("i", "y")
                print(word)

            else:
                print(word)
    except IndexError:
        print("ERROR (@function remove_suffix_ness): Function cannot process that word")


remove_suffix_ness('wellness')
remove_suffix_ness('sadness')
remove_suffix_ness('ridiculousness')
remove_suffix_ness('ordinariness')
remove_suffix_ness('heaviness')
remove_suffix_ness("nessness")
