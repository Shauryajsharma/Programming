def anagram_check():
    s = input()
    t = input()
    s = s.replace(" ","")
    t = t.replace(" ","")
    arr1 = []
    arr2 = []
    for i in s:
        arr1.append(i)
    for j in t:
        arr2.append(j)
    j=0
    list1 = sorted(arr1)
    list2 = sorted(arr2)
    if (list1==list2):
        return True
    else:
        return False

if anagram_check():
    print("Anagram strings")
else:
    print("Non Anagram Strings")
