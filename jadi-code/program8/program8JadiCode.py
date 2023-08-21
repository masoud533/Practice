n = 17

avval = True
for i in range(2,n):
    if n % i == 0:
        avval = False

if avval:
    print("It is prime")
else:
    print("not prime")