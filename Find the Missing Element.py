arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
n = len(arr1)
arr1.sort()
arr2.sort()
for i in range(n):
    for j in range(i,n-1):
        if (arr1[i] == arr2[j]):
            break
        else:
            print(arr1[i], ' is the missing number')
