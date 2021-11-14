def fibonacci_generator(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        # yield b
        b = c
    return b


def main():
    months = int(input("Anna kuukausien lukumäärä: "))
    amount = fibonacci_generator(months)
    print(f"Kanipariskuntia on {months} kuukauden kuluttua {amount}")


if __name__ == '__main__':
    main()
