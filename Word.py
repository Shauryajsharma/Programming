string = input()
count1 = 0
count2 = 0
for char in string:
    if char.isupper():
        count1 += 1
    elif char.islower():
        count2 += 1

if (count2 >= count1):
    print(string.lower())

else:
    print(string.upper())
