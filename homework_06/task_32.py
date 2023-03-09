from random import randint

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

my_list = [randint(1,1000) for _ in range(20)]
print(*my_list, sep=', ', end='\n')

min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

indexes = [i for i in range(len(my_list)) if min < my_list[i] < max]
print(*indexes, sep=', ', end='')