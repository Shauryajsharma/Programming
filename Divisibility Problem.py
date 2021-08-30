n = int(input())
for i in range(0,n):
    a,b = map(int,input().split())
    count = 0
    while (a%b != 0):
        a += 1
        count += 1
    if (a%b == 0):
        print(count)
