def way_too_long(word):
	x = len(word)
	if x > 10:
		print(f'{word[0]}{x-2}{word[-1]}')
	else:
		print(word)
n = int(input())

for i in range(n):
	word = input()
	way_too_long(word)
	