number = int(input('enter your number: '))

X = 1
while X != number+1:
    print((str(X) + ' ') * X)
    X += 1
X -=2
while X != 0:
    print((str(X) + ' ') * X)
    X -= 1 
