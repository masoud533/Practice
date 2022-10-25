<<<<<<< HEAD
import math


is_primal = lambda n: not[i for i in range(2,int(math.sqrt(n) + 1)) if not (n % i)]
primal_in_range = lambda n: [i for i in range(2,n+1) if is_primal(i)]

=======
import math


is_primal = lambda n: not[i for i in range(2,int(math.sqrt(n) + 1)) if not (n % i)]
primal_in_range = lambda n: [i for i in range(2,n+1) if is_primal(i)]

>>>>>>> 452e4debdf5d4398962ac36ac181e47675977123
print(primal_in_range(100))