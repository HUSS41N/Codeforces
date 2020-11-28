n = input()
n = list(map(int,n.split('+')))
n.sort()
x = ''
for i in range(len(n)):
    x += str(n[i]) + '+'
print(x[0:-1])