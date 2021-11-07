def prime_func(start, end):
    prime_number_count = 0
    last_prime = 2
    numbers_checked = 0

    while start < 2:
        if start == 1 or start == 0:
            print(f"{start} ei ole kelvollinen alkuluku.")
            numbers_checked += 1
            start += 1

    for num in range(start, end + 1):

        for i in range(2, num):  # Checking if the number is dividable by any number before itself
            if (num % i) == 0:
                print(f"{num} ei ole alkuluku, koska {i} * {int(num/i)} = {int(num/i) * i}")
                break
        else:
            print(f"{num} on alkuluku.")
            prime_number_count += 1
            last_prime = num

        numbers_checked += 1

    if prime_number_count >= 1:
        print(f"Tutkittiin {numbers_checked} lukua, joista {prime_number_count} oli alkulukuja.")
        print(f"Viimeinen löydetty alkuluku oli {last_prime}.")
    else:
        print("Testialueelta ei löytynyt alkulukuja.")


def main():
    start_num = int(input("Anna alueen alaraja: "))
    end_num = int(input("Anna alueen yläraja: "))

    prime_func(start_num, end_num)

    print("Kiitos ohjelman käytöstä.")


main()
