a = int(input())
b = int(input())
c = int(input())
exp1 = a+b*c
exp2 = a*(b+c)
exp3 = a*b*c
exp4 = (a+b)*c
if (exp1>=exp2 and exp1>=exp3 and exp1>=exp4):
    print(exp1)
elif (exp2>=exp1 and exp2>=exp3 and exp2>=exp4):
    print(exp2)
elif (exp3>=exp1 and exp3>=exp2 and exp3>=exp4):
    print(exp3)
elif (exp4>=exp2 and exp4>=exp3 and exp4>=exp1):
    print(exp4)
