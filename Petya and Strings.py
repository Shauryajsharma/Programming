def lexo():
    str1 = input()
    str2 = input()
    str1 = str1.upper()
    str2 = str2.upper()
    if (str1>str2):
        print("1")
    elif (str1<str2):
        print("-1")
    elif (str1==str2):
        print("0")
lexo()
