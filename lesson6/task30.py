#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
numb_one=int(input('первый элимент = '))
difference=int(input('разность = '))
numb=int(input('количество элементов = '))
arr=[]
for i in range(numb):
    arr.append(numb_one + (i) * difference)
print(arr)



# 5 8 11 14 17 20 23 26 29 32
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)