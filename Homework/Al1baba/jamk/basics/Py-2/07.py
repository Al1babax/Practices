numbers = []

for x in range(3):
    a = input(f"Input integer {x + 1}: ")
    numbers.append(a)

numbers.sort(key=int)
print(f"Max value: {numbers[-1]}")
