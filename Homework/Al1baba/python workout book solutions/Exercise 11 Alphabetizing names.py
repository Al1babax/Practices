from operator import itemgetter
PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
          ]

def alphabetize_names(data):
    """
    data.sort(key=itemgetter("first"))
    print(data)
    data.sort(key=itemgetter("last"))
    print(data)
    """
    # first_name_sort = sorted(data, key=lambda x: x["first"])
    # print(first_name_sort)
    for p in sorted(data, key=lambda x: [x['last'], x['first']]):
        print(f'{p["last"]}, {p["first"]}: {p["email"]}')


# alphabetize_names(PEOPLE)

def sort_by_absolute_value(seq1):
    # Making a function that returns the absolute value
    a = lambda x: (x - x) - x if x < 0 else x  # Python doesnt like this :D
    new_list2 = sorted(seq1, key=a)
    # new_list = list(map(a, seq1))
    print(new_list2)


a = [-5, 7, -3, 4, -1, -6, 2]
# sort_by_absolute_value(a)




