def str_sort(str1):
    char_dict = {x: ord(x) for x in str1}

    sorted_by_value = {k: v for k, v in sorted(char_dict.items(), key=lambda v: v[1])}
    print(sorted_by_value)

str_sort("cbadfmgkldfjklgmkldfgmldfmkgig")
