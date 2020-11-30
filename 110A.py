n = input()
count = 0
for i in n:
    if i == '4' or i == '7':
        count += 1
x_count = 0
for i in str(count):
    if i == '4' or i == '7':
        x_count += 1
if x_count == len(str(count)):
    print('YES')
else:
    print('NO')
