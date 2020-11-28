k,n,w = input().split()
# #k = cost of the first banana
# #n = money he has
# #w = number of banana he wants
count = []
for i in range(1,int(w)+1):
    count.append(i*int(k))
if sum(count) > int(n):
    print(sum(count)-int(n))
else:
    print(0)