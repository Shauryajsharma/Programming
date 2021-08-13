a,b = input().split()
a = int(a)
b = int(b)
years = 0

while (a<=b):
    a = 3*a
    b = 2*b
    years += 1

print(years)
