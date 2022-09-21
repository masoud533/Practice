from is_primal import is_primal
def number(n):
    if n == 1:
        return 'one is not primal'
    elif n == 0:
        return 'Zero is not primal'
    primalList = []
    for i in range(2, n+1):
        if is_primal(i):
            primalList.append(i)
    return f'Between 1 and {n} prime numbers are: {primalList}'

while True:
    try:
        num = int(input('enter your number: '))
        break
    except ValueError:
        print('ops, Please enter a number!!!')
print(number(num))