from random import randint

# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

size = int(input('Введите длину списка: '))
list = [randint(1,100) for i in range(size)]
print(list)

values = set(list)
value_list = sorted(values)

count_dict = {}
for item in value_list:
    count_dict[item] = 0
    for it in list:
        if item == it:
            count_dict[item] += 1
# print(count_dict)

found_number = int(input('Введите число, которое нужно найти: '))

if count_dict.get(found_number, 0) > 0:
    print(f'В заданном списке число {found_number} встречается {count_dict[found_number]} р.')
else:
    count = 0
    close_number = 0
    for i in range(len(value_list)):
        temp = abs(value_list[i] - found_number)
        if count > temp or count == 0:
            count = temp
            close_number = value_list[i]
    print(f'В заданном списке число {found_number} не встречается. Но ближайшее число {close_number} встречается {count_dict[close_number]} р.')