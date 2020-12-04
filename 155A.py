n = int(input())
points = list(map(int,input().split()))
smallest = points[0]
largest = points[0]
count = 0
for point in points[1:]:
    if smallest > point:
        smallest = point
        count+= 1
    if point > largest:
        largest = point 
        count +=1
print(count)