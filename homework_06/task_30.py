# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый член арифметической прогрессии: '))
difference = int(input('Введите разность арифметической прогрессии: '))
quantity = int(input('Введите количество элементов арифметической прогрессии: '))
my_array = [first_element+(i-1)*difference for i in range(1, quantity)]

print(*my_array, sep='\n')