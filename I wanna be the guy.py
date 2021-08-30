n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list1.pop(0)
list2.pop(0)
for i in list2:
    list1.append(i)
list1.sort()
if (list1[-1] == n):
    print('I become the guy')
else:
    print('Oh, my keyboard!')
