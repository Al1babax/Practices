def first_last(data):
    result = [data[0], data[-1]]
    return result


func1 = lambda data: [data[0], data[-1]]    # Basically same thing as above function

a = [1, 2, 3, 4]
b = "abc"
c = (1, 2, 3, 4, 5, 6)

print(first_last(a))
print(func1(a))

print(first_last(c))

print(first_last(b))
print(func1(b))



def sum_odd_even(list1):
    even_list = [list1[i] for i in range(len(list1)) if i % 2 == 0]
    odd_list = [list1[i] for i in range(len(list1)) if i % 2 != 0]
    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    return [even_sum, odd_sum]


test1 = [10, 20, 30, 40, 50, 60]
print(sum_odd_even(test1))


def plus_minus(data):
    l1 = [x - (x * 2) for y, x in enumerate(data) if y % 2 == 0]# Makes list of every other item and makes them negative
    l1.pop(0)
    value = sum(data) + (sum(l1) * 2)   # Adds even/odd values from the list so the result will be 10+20-30+40-50...
    return value


print(plus_minus([10, 20, 30, 40, 50, 60]))


def myzip(data1, data2):
    result = []

    for value in range(len(data1)):
        result.append((data1[value], data2[value]))

    return result


print(myzip([10, 20, 30], 'abc'))









