import numpy as np
def lcm(X, y):
    lX = []
    ly = []
    if (X  <= 10000) and  (y <= 10000):
        for i in range(1, y+100):
            lX.append(X * i)
        for i in range(1, X+100):
            ly.append(y * i)
        res = np.unique([j for j in lX + ly if j  in lX and j in ly])
        return res.min()
    else:
        return 'Please enter a smaller number'

print(lcm(13, 10000))