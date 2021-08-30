def pangram():
    n = int(input())
    s = input()
    string = s.upper()
    for i in range(0,n):
        count = string.count(string[i],i,n)
        if count>1:
            return False
    return True
            
        
if pangram():
    print("YES")
else:
    print("NO")
