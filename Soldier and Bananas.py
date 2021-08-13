k,n,w = input().split()
k = int(k)
n = int(n)
w = int(w)
total_cost = int(k*w*(w+1)/2)
borrow = total_cost - n
if borrow > 0:
    print(borrow)

else:
    print("0")
