def shift(l: list = [0,1,2,3,4],i: int =2, x: str = 'Right') -> list:
    if x == 'Right' or x == 'right' and i >= 0:
        return l[-i::] + l[:-i:]
    elif x == 'Left' or x == 'left' and i >= 0:
        return l[i::] + l[:i:]
    elif i < 0:
        return l[i::] + l[:i:]
    else:
        return 'ops! something went wrong, please try again'
print(shift(x='left', i=-2))