from typing import Callable, Any, List


def first_last(data):
    result = [data[0], data[-1]]
    return result


func1: Callable[[Any], list[Any]] = lambda data: [data[0], data[-1]]    # Basically same thing as above function

a = [1, 2, 3, 4]
b = "abc"

print(first_last(a))
print(func1(a))

print(first_last(b))
print(func1(b))














