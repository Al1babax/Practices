import random


def gensquares(N):
    for x in range(N):
        yield x ** 2


def square_test():
    for x in gensquares(10):
        print(x)


def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)


def rand_test():
    for num in rand_num(1, 10, 12):
        print(num)


def hello():
    s = "hello"
    s_iter = iter(s)
    for letter in s_iter:
        print(letter)


def extra_credit():
    my_list = [1, 2, 3, 4, 5]
    # Apparently comprehensions create generators when using ()
    gencomp = (item for item in my_list if item > 3)

    print(type(gencomp))

    for item in gencomp:
        print(item)


# square_test()
# rand_test()
# hello()
# extra_credit()



