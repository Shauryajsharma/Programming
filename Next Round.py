n,k = input().split()
n = int(n)
k = int(k)
arr = list(map(int,input().split()))
count = 0
for i in range(n):
    if (arr[k-1] <= arr[i] and arr[i]>0):
        count += 1
print(count)
