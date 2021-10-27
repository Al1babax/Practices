def dictdiff(d1, d2):
    result = {}

    for key in d1:

        if key not in d2 or d1[key] != d2[key]:
            result[key] = [d1.get(key), d2.get(key)]

    for key in d2:

        if key not in d1 or d1[key] != d2[key]:
            result[key] = [d1.get(key), d2.get(key)]

    return result


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

#print(dictdiff(d1, d1))
#print(dictdiff(d1, d2))

d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
#print(dictdiff(d3, d4))

d5 = {'a': 1, 'b': 2, 'd': 4}
#print(dictdiff(d1, d5))


def combine_dicts(*dicts):
    final_dict = {}
    for dict1 in dicts:
        final_dict.update(dict1)
    return final_dict


# print(combine_dicts(d1, d2, d3, d4, d5))

def make_dict(*data):
    result = {}

    for value in range(0, len(*data), 2):
        result[data[0][value]] = data[0][value + 1]

    return result


# print(make_dict(('a', 1, 'b', 2)))  # Expected output {'a': 1, 'b': 2}


def disc_partition(dict, func):
    dict1, dict2 = {}, {}

    for key, value in dict.items():     # Iterating though the dictionary to check whether they pass the function
        if func(value):
            dict1[key] = value
        else:
            dict2[key] = value

    return dict1, dict2


# print(disc_partition(d1, lambda x: x > 2))

