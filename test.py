n = 10
for i in range(1, n + 1):
    print(*[j*i for j in range(1, n+1)], sep='\t')