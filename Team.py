n = int(input())
count = 0
for i in range(n):
    views = input()
    prob = views.count('1')
    if (prob >= 2):
        count += 1
    else:
        continue

print(count)
