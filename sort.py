from random import randint  #вызываем функцию random

# Сортировка пузырьков
list_1 = []  #создаем список в котором 100 элементов
for i in range(0,100): 
    list_1.append(randint(0, 1_000_000))
list_1
len(list_1) 
#проверяем кол-во элеменов

m = 0 #количество сортировок
k = True # stop_flag
while k is True: # Цикл остановится когда k = True
    k = False
    for i in range(0, len(list_1) - 1): # перебираем весь список (0,100]
        for y in range(0, len(list_1) - 1):  # перебираем весь список (0,100]
          m += 1     
          if list_1[i] < list_1[i + 1]:
            a = list_1[i]
            list_1[i] = list_1[i + 1]
            list_1[i + 1] = a
            k =True 
print(list_1)
print("количество сортировок",m)

# Cортировка выбором
list_2 = list_1
list_1 = []
m_2 = 0
for i in range(0 ,len(list_2)):
    min = i
    for j in range(i + 1,len(list_2)):
        m_2 += 1
        if list_2[j] > list_2[min]:
            min = j
    b = list_2[i]
    list_2[i] = list_2[min]
    list_2[min] = b


print(f"Первый отсортированный список:{list_1}")
print(f"Второй отсортированный список:{list_2}") 
print(f'количество сравнений в первом списке:{m}')
print(f'количество сравнений во втором списке:{m_2}')
print(list_1)
print("кол-во сортировок",list_2)
