n,k = input().split()
for i in range(int(k)):
    if n[-1] == '0':
        n = n[:-1] 
    elif n[-1] != '0':
        n = int(n) - 1
        n = str(n)
print(n)