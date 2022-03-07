def largest_number(l1):     # Build in way ---> other way probably using loop
    return max(l1)


def other_way(l1:list):
    if len(l1) >= 1:
        max_number = l1[0]
        for num in l1:
            if num > max_number:
                max_number = num
        return max_number
    return False


print(largest_number([1, 5, 25, -5, 0.2, 2]))
print(other_way([1, 5, 25, -5, 0.2, 2]))
