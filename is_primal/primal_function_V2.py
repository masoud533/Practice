import math


is_primal = lambda n: not[i for i in range(2,int(math.sqrt(n) + 1)) if not (n % i)]
primal_in_range = lambda n: [i for i in range(2,n+1) if is_primal(i)]

print(primal_in_range(100))