import math
numbers = range(1, 1001)

primeNum = []

for num in numbers:
    Division = []
    if num != 1 and num != 0:
        for x in range(1, round(math.sqrt(num) + 1)):
            if (num  % x) == 0:
                Division.append(x)
        if len(Division) <= 1:
            primeNum.append(num)
print(primeNum)