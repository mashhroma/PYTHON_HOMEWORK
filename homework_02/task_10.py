import random

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

quantity = int(input('Введите количество монеток: '))
count =0

for i in range(quantity):
    coin = random.randint(0,1)
    if coin == 0:
        count +=1
    print(i+1, '==', 'решка' if coin == 0 else 'орел')

print(f'Нужно перевернуть {count} монеток.')