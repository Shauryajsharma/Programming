m,n = input().split()
m = int(m)
n = int(n)
if( (m*n)%2 == 0):
    print((m*n)//2)
else:
    print(((m*n)-1)//2)
