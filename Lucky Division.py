def division():
    n = int(input())
    list1= [4,7,44,47,74,77,444,447,477,744,747,777]
    for i in range(0,12):
        if n%list1[i] == 0:
            return True

    return False


if division():
    print("YES")
else:
    print("NO")
        
