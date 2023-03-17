# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

from phonebase import *

base = 'phones.txt'
phone_book = BASE_OPEN(base)

help = (' ------------------------------------------'
        '\n Возможные действия:'
        '\n 1 - help   Подсказка'
        '\n 2 - save   Сохранить файл телефонной книги'
        '\n 3 - show   Показать все контакты'
        '\n 4 - find   Найти контакт'
        '\n 5 - add    Добавить контакт'
        '\n 6 - chng   Изменить контакт'
        '\n 7 - del    Удалить контакт'
        '\n 8 - exit   Выход'
        '\n 9 - copy   Скопировать файл телефонной книги'
        '\n ----------------------------------------')
print(help)

flag = True

while flag:
    print()
    action = input('Введите номер задачи (для справки - help): ')

    if action == '1' or action == 'help':
        print(help)

    if action == '2' or action == 'save':
        SAVE_BASE(base, phone_book)
        print('Данные в справочнике сохранены')

    if action == '3' or action == 'show':
        SHOW_BASE(base)

    if action == '4' or action == 'find':
        find = input('Найти: ')
        print(FIND_CONTACT(base, find))

    if action == '5' or action == 'add':
        add_data = input('Добавить (телефон, Ф.И.О.): ')
        ADD_CONTACT(phone_book, add_data)
        print('Запись добавлена. Сохранить изменения в справочнике - команда "2" (save)')

    if action == '6' or action == 'chng':
        find_change = input('Найти контакт: ')
        find_list = FIND_INDEX(phone_book, find_change)
        if len(find_list) < 1:
            print('В справочнике нет таких данных.')
        else:
            print('В справочнике нашлись следующие записи:')
            for i in find_list:
                print(f'Запись {i}: {phone_book[i]}')
            change_item = int(input('Выберите номер записи, которую нужно изменить: '))
            change_data = input('Новые данные: ')
            phone_book[change_item] = change_data
            print('Запись изменена. Сохранить изменения в справочнике - команда "2" (save)') 

    if action == '7' or action == 'del':
        find_del = input('Введите данные для удаления: ')
        find_list_for_del = FIND_INDEX(phone_book, find_del)
        if len(find_list_for_del) < 1:
            print('В справочнике нет таких данных.')
        else:
            print('В справочнике нашлись следующие записи:')
            for i in find_list_for_del:
                print(f'Запись № {i} - {phone_book[i]}')
            del_item = int(input('Выберите номер записи, которую нужно удалить: '))
            phone_book.pop(del_item)
            print('Запись удалена. Сохранить изменения в справочнике - команда "2" (save)')

    if action == '8' or action == 'exit':
        exit_status = input('Работа будет окончена. Чтобы сохранить изменения нажмите Y, а затем команду "2"(save).'
                            '\nДля выхода без сохранения нажмите любую клавишу: ').lower()
        if exit_status == 'y':
            flag = True
        else:
            flag = False
    
    if action == '9' or action == 'copy':
        new_file = input('Введите название нового файла: ')+'.txt'
        SAVE_BASE(new_file, phone_book)
