import math
def number(n):
    primal = []
    for i in range(2, n):
        X = []
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                X.append(j)
        if len(X) == 0:
            primal.append(i)
    return primal


while True:
    try:
        primalList = int(input('enter your number: '))
        break
    except ValueError:
        print('ops, Please enter a number!!!')
else:
    print('number imported!!!')

print('list of primal: ' , number(primalList))