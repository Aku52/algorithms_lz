'''from random import randint
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
'''


from random import randint  #вызываем функцию random

list_1 = []  #создаем список в котором 100 элементов
for i in range(0,100): 
    list_1.append(randint(0, 1_000_000))
list_1
len(list_1) #проверяем кол-во элеменов

n = list_1
m = 0
k = True
while k is True: # Цикл остановится когда stop_flag = True
    k = False
    for i in range(0, len(list_1) - 1): #перебираем весь список начиная с 0 элемента и до 101, но от списка - 1 элемент и в итоге перебираем 100 элементов 
        for y in range(0, len(list_1) - 1): 
          m += 1     
          if list_1[i] < list_1[i + 1]:
            swap = list_1[i]
            list_1[i] = list_1[i + 1]
            list_1[i + 1] = swap
            k =True 
print(list_1)
print("кол-во сортировок",m)

list_2 = list_1
list_1 = []
list_2 = 0
while len(list_2) > 0:
    max = list_2[0]
    for i in range(0, len(list_2)):
     for t in range(0, len(list_2)):
        list_2 += 1
        if list_2[i] > max:
            max = list_2[i]
    list_1.append(max)
    list_2.remove(max)

print(list_1)
print("кол-во сортировок",list_2)
