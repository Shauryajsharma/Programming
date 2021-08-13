num =int(input())
count = 0
n = num
while(n != 0):
    n = int(n/10)
    count += 1
new_count = 0
next_count = 0
for i in range(count):
    digit = num % 10
    num = int(num/10)
    if (digit == 4) or (digit == 7):
        new_count += 1

    if (digit != 4) and (digit != 7):
        next_count += 1
        
newer_count = next_count

while (newer_count != 0):
    print("NO")
    newer_count = 0
    break

while (new_count != 0) and (next_count == 0):
    if ((new_count==4) or (new_count==7)):
        print("YES")
        new_count = 0
        break

    else:
        print("NO")
        new_count = 0
        break

    
