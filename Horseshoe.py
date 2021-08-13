a,b,c,d = map(int,input().split())
count = 0
if (a!=b and a!=c and a!=d):
    count += 1
if (b!=c and b!=d):
    count += 1
if(c!=d):
    count += 1

print(3-count)
