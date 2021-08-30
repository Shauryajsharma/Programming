n = int(input())
list1 = []
count = 0
for i in range(n):
    s = input()
    list1.append(s.upper())
for i in range(n):
    if(list1[i][0] == 'T'):
        count += 4
    if(list1[i][0] == 'C'):
        count += 6
    if(list1[i][0] == 'O'):
        count += 8
    if(list1[i][0] == 'D'):
        count += 12
    if(list1[i][0] == 'I'):
        count += 20

print(count)
