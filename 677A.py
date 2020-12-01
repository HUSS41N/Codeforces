n,h = input().split()
ns = list(map(int,input().split()))
count = 0
for i in ns:
    if int(h) > i or int(h) == i:
        count += 1
    elif int(h) < i:
        count += 2
print(count)