def product_fib(prod):
    product_list = {}
    fib_sequence = []

    for x in fibonacci_generator(5000):
        fib_sequence.append(x)

    for i in range(len(fib_sequence) - 1):
        product = fib_sequence[i] * fib_sequence[i + 1]
        product_list[product] = [fib_sequence[i], fib_sequence[i + 1]]

    if prod in product_list.keys():
        return [product_list[prod][0], product_list[prod][1], True]
    else:
        for key in product_list.keys():
            if prod < key:
                return [product_list[key][0], product_list[key][1], False]


def fibonacci_generator(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a + b
        a = b
        b = c
