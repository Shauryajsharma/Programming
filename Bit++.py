x = 0
n = int(input())
for i in range(n):
    exp = input()
    if ((exp[0] == '+') or (exp[2] == '+')):
        x += 1
    elif ((exp[0] == '-') or (exp[2] == '-')):
        x -= 1


print(x)
