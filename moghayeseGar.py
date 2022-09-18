def compare(X, y):
    str1 = X
    str2 = y
    while True:
        if len(str1) != 0 and len(str2) != 0:
            if str1[0] < str2[0]:
                str1 = str1[1:]
            elif str1[0] > str2[0]:
                str2 = str2[1:]
            else:
                str1 = str1[1:]
                str2 = str2[1:]
        if len(str1) != 0 and len(str2) == 0:
            return str1
        elif len(str1) == 0 and len(str2) != 0:
            return str2
        elif len(str1) == 0 and len(str2) == 0:
            return 'Both strings are empty!'
        str1 = str1[::-1]
        str2 = str2[::-1]