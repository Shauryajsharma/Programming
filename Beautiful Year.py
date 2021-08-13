n = int(input())
while n<9000:
    n += 1
    a = n/1000
    b = int((n%1000)/100)
    c = int(((n%1000)%100)/10)
    d = int(((n%1000)%100)%10)
    if (a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        break
print(n)
    
