#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
#Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. 
#Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
#на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. 
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
#находясь перед некоторым кустом заданной во входном файле грядки.
x = int(input('колическво кустов: '))
list_1 = []
for i in range(x):
  i = int(input('введите кол-во ягод на кусте: '))
  list_1.append(i)
print(list_1)
list_2 = []
for i in range(len(list_1)-1):
  list_2.append(list_1[i-1] + list_1[i] + list_1[i+1])
list_2.append(list_1[0] + list_1[x-1] + list_1[x-2])
print(list_2)
max = list_2[0]
for i in range(len(list_2)):
  if list_2[i] > max:
    max = list_2[i]
print('макс кол ягод', max)