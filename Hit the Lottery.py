n = int(input())
count = 0
a = [100,20,10,5,1]
for i in range(0,5):
    count += n//a[i]
    n = n%a[i]
print(count)
