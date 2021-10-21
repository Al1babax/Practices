def str_sort(str1):
    char_dict = {x: ord(x) for x in str1}

    print(sorted(char_dict))


str_sort("cbadfmgkldfjklgmkldfgmldfmkgig")
