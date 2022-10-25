<<<<<<< HEAD
n = int(input('hello: '))


x = lambda n: not [i for i in range(2, n) if not (n % i) ]
y = lambda n: [i for i in range(2, n+1) if x(i)]

=======
n = int(input('hello: '))


x = lambda n: not [i for i in range(2, n) if not (n % i) ]
y = lambda n: [i for i in range(2, n+1) if x(i)]

>>>>>>> 452e4debdf5d4398962ac36ac181e47675977123
print(y(n))