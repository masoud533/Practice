import numpy as np
def GCM(X, y):
    lX = []
    ly = []
    for i in range(1, X+1):
        if X % i == 0:
            lX.append(i)
    for i in range(1, y+1):
        if y % i == 0:
            ly.append(i)
    res = np.unique([j for j in lX + ly if j  in lX and j in ly])
    return res.max()


print(GCM(10, 200))