#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

n = int(input('enter n: '))
m = int(input('enter m: '))
list_1 = []
list_2 = []
for i in range(n):#заполняем первый список
  k = int(input('enter number: '))
  list_1.append(k)
print(list_1)

for i in range(m):#заполняем второй список
  k = int(input('enter number: '))
  list_2.append(k)
print(list_2)

list_3 = []#находим повторяющиеся элементы в обоих списках
for i in list_1:
  for j in list_2:
    if i == j:
      list_3.append(i)
      break
print(list_3)

list_4 = []#получаем список без повторов
for i in list_3:
  if i not in list_4:
      list_4.append(i)     
print(list_4)

for i in range(len(list_4)):#сортируем по возрастанию
  for j in range(len(list_4)):
    if list_4[i] < list_4[j]:
      list_4[i], list_4[j] = list_4[j], list_4[i]
print(list_4)
