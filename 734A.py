n = int(input())
s = input()
if s.count('A') == s.count('D'):
    print('Friendship')
elif s.count('A') > s.count('D'):
    print('Anton')
elif s.count('D') > s.count('A'):
    print('Danik')