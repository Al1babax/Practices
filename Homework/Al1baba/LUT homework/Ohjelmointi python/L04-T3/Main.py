a = int(input("Anna a:n arvo: "))
b = int(input("Anna b:n arvo: "))

mult_number = 2
add_number = 100

while True:
    print(f"a: {a} b: {b}")
    if a > b or a > 10_000 or b > 10_000:
        break
    a *= mult_number
    b += add_number

print("Kiitos ohjelman käytöstä.")







