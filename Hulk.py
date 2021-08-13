s1 = "I hate"
s2 = "I love"
s = ""
n = int(input())
for i in range(1,n+1):
    if (i == 1):
        s = s + s1
    elif (i != 1 and i%2 != 0):
        s = s + " that " + s1
    elif (i%2 == 0):
        s = s + " that " +s2
print(s + " it")
        
