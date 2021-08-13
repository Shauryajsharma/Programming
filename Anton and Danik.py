n = int(input())
s = input()
s = s.upper()
a = 0
d = 0
for i in s:
    if (i == 'A'):
        a += 1
    elif (i == 'D'):
        d += 1

if (a>d):
    print("Anton")

elif (a<d):
    print("Danik")

elif (a==d):
    print("Friendship")
