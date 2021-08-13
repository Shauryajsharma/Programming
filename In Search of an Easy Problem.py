n = int(input())
list1 = []
list1 = list(map(int,input().split()))
count = list1.count(1)
if (count>=1):
    print("HARD")
else:
    print("EASY")
