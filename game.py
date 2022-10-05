def game(number):
    n1 = int(str(number)[0])
    n2 = int(str(number)[1])
    maximum = n1 - n2 if n1 > n2 else n2 - n1
    return maximum