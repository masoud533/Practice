import math
def is_prime(n):
    avval = True
    for i in range(2,round(math.sqrt(n))):
        if n % i == 0:
            avval = False
            break
    return avval


prime_count = 0
last_prime_number = 0 
for i in range(1,1000001):
    if is_prime(i):
        prime_count += 1
        last_prime_number = i

print(f'we had {prime_count} prime number')
print(f"last prime number was {last_prime_number}")
