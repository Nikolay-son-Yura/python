# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# num_1 = [int(x) for x in input("Введите элементы первого множеств через пробел ").split()]
# num_2 = [int(x) for x in input("Введите элементы второго множеств через пробел ").split()]

# n = int(input("Ведите кол-во элементов первого множества "))
# m = int(input("Ведите кол-во элементов второго множества "))

num_1 =[1, 2, 3, 7, 9, 6, 1, 1, 1, 1, 1, 1, 1, 0, 5]
num_2 =[2, 9, 7, 6, 0, 0,9,8,7,6,5,4, 0, 0, 0, 1, 5]

# for i in range(n):
#     i=int(input('Введите элементы первого множеств через Enter= '))
#     num_1.append(i)
# for j in range(m):
#     j=int(input('Введите элементы второго множеств через Enter= '))
#     num_2.append(j)

print(f"первый список{num_1}")
print(f"второй список{num_2}")

list_general=[]
for i in num_1:
    for j in num_2:
        if i==j:
            list_general.append(i)
print(set(list_general))
# set_1=set(num_1)
# set_2=set(num_2)
# list_general = sorted(set_1.intersection(set_2))  # нашел на просторах инета
# print(*sorted(num_1 and num_2))# или так






