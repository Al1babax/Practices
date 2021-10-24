def my_sum(*args):
    if not args:
        return args

    result = args[0]  # Setting first value to make the variable object

    for value in range(len(args) - 1):
        result += args[value + 1]

    return result


def my_sum_bigger_than(threshold, *args):  # first parameter is the min value for the sum
    new_data = list(filter(lambda value: value > threshold, args))
    result = new_data[0]

    for i in range(len(new_data) - 1):
        result = my_sum(result, new_data[i + 1])

    print(result)


def sum_numeric(*data):
    data_list = [x for x in data]
    remove_list = []

    for i in range(len(data_list)):
        try:
            data_list[i] = int(data_list[i])
        except:
            print(f"cannot do for value {data_list[i]}")
            remove_list.append(data_list[i])

    for value in remove_list:
        data_list.remove(value)

    result = data_list[0]

    for i in range(len(data_list) - 1):
        result = my_sum(result, data_list[i + 1])

    print(result)


# my_sum('abc', 'def')
# my_sum([1, 2, 3], [4, 5, 6])
# my_sum(1, 2, 3)
# my_sum((1, 2), (3, 4))
# my_sum_bigger_than(10, 5, 20, 30, 6)
sum_numeric(10, 20, 'a', '30', 'bcd')
