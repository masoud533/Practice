import math
def is_primal(n):
    if n in [0, 1]:
        return False
    X = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            X.append(i)
    if len(X) == 0:
        return True
    else:
        return False
 
