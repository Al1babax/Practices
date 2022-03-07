def josephus_survivor(n: int, k):
    n_list = [x + 1 for x in range(n)]
    index_number = 0
    while len(n_list) > 1:
        index_number += k - 1
        print(f"Index number is now {index_number} ja lista on {len(n_list)} pitkä")
        if index_number >= len(n_list):
            index_number = index_number % len(n_list)
        n_list.pop(index_number)

    return n_list[0]


print(josephus_survivor(7, 3))
