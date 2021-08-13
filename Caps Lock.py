s = input()
length = len(s)
count = 0
new = ''
for i in range(0,length):
    if s[i].isupper():
        count += 1

if (count==length):
    print(s.lower())
if (count==length-1 and s[0].islower()):
    new = s[0].upper()
    print(new + s[1:].lower())
if (count!=length and count!=length-1):
    print(s)
