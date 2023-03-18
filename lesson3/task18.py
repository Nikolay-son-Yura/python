# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
#  6
# -> 5
import random

n = int(input("количество элементов в массиве N= "))
x = int(input("какое число X= "))  # проблемы с цифрой 1
new_list = []
numb = 0
numb_less = 0
numb_more = 0
y = 0
for i in range(n):
    i=random.randint(1,30)
    new_list.append(i)
print(new_list)
for j in new_list:
    if j == x:
        numb = j
        y = 1
    elif j < x and j - x > numb_less - x:
        numb_less = j
       
    elif j > x and numb_more - j < j + x:
        print(f"j{j}")
        numb_more = j
        print(f"more{numb_more}")
        

print(numb_less, numb, numb_more)
