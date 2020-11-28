s = input()
lower = 0
upper = 0
for i in s:
	if i == i.lower():
		lower += 1 
	elif i == i.upper():
		upper += 1
if lower > upper or lower == upper :
	print(s.lower())
else:
	print(s.upper())