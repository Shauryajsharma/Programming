n,k = input().split()
n = int(n)
k = int(k)
b = 240-k
count = 0
sum1 = 0
for i in range(1,n):
    sum1 = sum1 + (5*i)
    if (sum1 <= b):
        count += 1
    else:
        break
print(count)
