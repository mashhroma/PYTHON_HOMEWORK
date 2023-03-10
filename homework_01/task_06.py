# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите трехзначное число: '))
num_01 = ticket % 10
num_02 = (ticket//10) % 10
num_03 = (ticket//100) % 10
num_04 = (ticket//1000) % 10
num_05 = (ticket//10000) % 10
num_06 = (ticket//100000) % 10
first_sum = num_01+num_02+num_03
second_sum = num_04+num_05+num_06

if first_sum == second_sum:
    print(f'Билет с номером {ticket} - счастливый!')
    print(f'Сумма {num_01}+{num_02}+{num_03} равна сумме {num_04}+{num_05}+{num_06}.')
else:
    print(f'Билет с номером {ticket} не является счастливым.')
    print(f'Сумма {num_01}+{num_02}+{num_03} не равна сумме {num_04}+{num_05}+{num_06}.')
