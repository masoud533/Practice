def shift(l: list = [0,1,2,3,4],i: int =2, x: str = 'Right') -> list:
    i %= len(l)
    if x == 'Right' or x == 'right' or x == 'r' and i >= 0:
        return l[-i::] + l[:-i:]
    elif x == 'Left' or x == 'left' or x == 'l' and i >= 0:
        return l[i::] + l[:i:]
    elif i < 0:
        return l[i::] + l[:i:]
    else:
        return 'ops! something went wrong, please try again'
print(shift(x='l', i=12))