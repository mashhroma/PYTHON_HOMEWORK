import random
import math

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 3+4=7
# 3*4=12
# s = x+y
# p = x*y

s=7
p=12

print(f'Сумма двух чисел равна {s}.')
print(f'Произведение двух чисел равно {p}.')

D = s*s - 4*p
x = (s - math.sqrt(D))/2
y = s-x


print(f'Загаданные числа:')
print('X = ', int(x))
print('Y = ', int(y))