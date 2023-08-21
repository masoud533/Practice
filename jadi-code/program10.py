def Zarib3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

sum = 0   
for i in range(1, 10):
    #print(f"checking: {i}")
    if Zarib3or5(i):
        #print(f"zarib is fine for {i}")
        sum += i
        #print(f"sum is {sum}")
print(sum)