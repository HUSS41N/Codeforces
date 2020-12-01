n = int(input())
ns = map(int,input().split())
d = {}
for k,v in enumerate(ns):
    d[v] = k+1
for i in range(n):
    print (d[i+1],end=' ')