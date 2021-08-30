n,k = input().split()
n = int(n)
k = int(k)
list1 = []
for i in range(1,n+1,2):
    list1.append(i)
for i in range(2,n+1,2):
    list1.append(i)
print(list1[k-1])

    
        
    
               
