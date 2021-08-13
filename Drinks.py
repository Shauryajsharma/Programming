n = int(input())
list1 = []
list1 = list(map(int,input().split()))
sum1 = 0
for j in range(n):
    sum1 += list1[j]
print(sum1/n)
