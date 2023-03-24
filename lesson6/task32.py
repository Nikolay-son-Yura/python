# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

min_numb = int(input("Введите минимум ="))
max_numb = int(input("Введите максимум ="))
list_one = []#[2, 5, 1, -3, 2, 8, 1, -6, 9, -9, 6, 0, 7, -1, 8, -4, 6, -5, 10, -1]
list_two = []
for i in range(20):#так захотелось
    i=random.randint(-10,10)
    list_one.append(i)
print(list_one)

for j in range(len(list_one)):
    if min_numb <= list_one[j] <= max_numb:
        list_two.append(j)
print(f"индексы диапазона от {min_numb} до {max_numb} = {list_two}")
