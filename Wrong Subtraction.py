n,k = input().split()
n = int(n)
k = int(k)

while (k>1):
    if (n%10 == 0):
        n = int(n/10)
        if (n==1):
            break
            

    else:
        n = n-1
        k = k-1
        if (n == 1):
            break            


print(n)
