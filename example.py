n = int(input('hello: '))


x = lambda n: not [i for i in range(2, n) if not (n % i) ]
y = lambda n: [i for i in range(2, n+1) if x(i)]

print(y(n))