def game(number):
    n1 = int(str(number)[0])
    n2 = int(str(number)[1])

    if n1 >= n2:
        return n1 - n2
    elif n2 > n1:
        return n2 - n1