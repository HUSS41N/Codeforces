t = int(input())
arr = []
for i in range(t):
    x = input()
    arr.append(x)
def sum(num):
    count = 0
    for i in range(num+1):
        count += i
    return count
def numsum(num):
    sum = 0
    for i in range(num,0,-1):
        sum += 1
    return (sum-1)*10

for i in arr:
    if len(i) == 1:
        print(1)
    else:
        x = sum(len(i))
        if x >= 10:
            print(int(i[0])*10)
        else:
            z = numsum(int(i[-1]))
            print(x+z)