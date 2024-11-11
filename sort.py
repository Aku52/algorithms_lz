from random import randint
list_1 = list ()
for i in range (1,100):
    list_1.append(randint(0,1000000))

m = 0
k = 0
n = len(list_1)
for i in range (n):
    for j in range (0, n-i-1):
        m += 1
        if list_1[j]< list_1[j+1]:
            k += 1
            list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
return m, k
 
print(list_1)




