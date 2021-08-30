s = input()
stringlist = s.split()
for i in range(len(stringlist)):
    print(stringlist[-1], end = " ")
    stringlist.pop()
