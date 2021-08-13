s = 'hello'
def room():
    x = 0
    string = input()
    for i in range(len(string)):
        if (s[x] == string[i]):
            x += 1
            if x==5:
                break
    if x == 5:
        return True
    else:
        return False


if room():
    print("YES")

else:
    print("NO")
