n = int(input())
for i in range(0,n):
    k = int(input())
    list1 = []
    list1 = list(map(int,input().split()))
    for j in range(0,len(list1)):
        if (j==0):
            if (list1[j] != list1[j+1] and list1[j] != list1[j+2] and j==0):
                print("1")
                break
            elif (list1[j] != list1[j+1] and list1[j] == list1[j+2] and j==0):
                print('2')
                break
        elif (list1[j] != list1[j+1]):
            print(j+2)
            break
