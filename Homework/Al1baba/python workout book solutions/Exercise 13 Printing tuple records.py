from collections import namedtuple
PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]


def format_sort_records(data):
    template = "{1:10} {0:10} {2:5.2f}"
    for person in data:
        print(template.format(person[0], person[1], person[2]))


# format_sort_records(PEOPLE)

people_tuple = namedtuple("people_tuple", "Surname, First_name, Arrival_time")
trump = people_tuple("Trump", "Donald", 7.85)
putin = people_tuple("Putin", "Vladimir", 3.626)
xi = people_tuple("Xi", "Jinping", 10.603)
# print(trump._asdict())
# print(putin._asdict())
# print(xi._asdict())


NOMINATED = [
    ("Ice age", 130, "Pelle Hermanni"),
    ("Lord of the rings", 200, "Ronald McDonald"),
    ("Matrix", 250, "Keanu Reeves")
]


def sort_list(data, sort_value):
    list_format = "{0:20} {1:5} {2:20}"
    if sort_value.lower() not in "name length director":
        print("You did not give parameter to sort with")
        return
    operation = {       # Setting all operations
        "name": 0,
        "length": 1,
        "director": 2
    }
    a = sorted(data, key=lambda x: x[operation[sort_value.lower()]])    # Sorting the list with given sort_value
    for element in a:
        print(list_format.format(element[0], element[1], element[2]))   # loop printing according the list_format


# sort_list(NOMINATED, input("What you want the list to be sorted as (Name, Length, Director)? "))

