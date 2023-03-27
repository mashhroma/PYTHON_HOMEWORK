import classes
import view
import texts

phone_book = classes.PhoneBook('phone_base.txt')
view.main_menu(texts.help)
my_phone = phone_book.open_book

while True:
    choice = input('Выберите пункт меню (для справки нажмите "7" или help): ')
    match choice:
        case '1' | 'show': # посмотреть контакты
            print(phone_book)

        case '2' | 'find': # найти контакт
            find_word = view.get_search()
            search = phone_book.find_contact(find_word)
            if len(search) < 1:
                print('Данные не обнаружены.')
            else:
                print(search)

        case '3' | 'add': # добавить контакт
            change_contact = view.get_contact()
            phone_book.add_contact(change_contact)
            view.show_message(texts.add_text)

        case '4' | 'change': # изменить контакт
            find_word = view.get_search()
            search = phone_book.find_contact(find_word)
            if len(search) < 1:
                print('Данные не обнаружены.')
            else:
                print(search)
                index = view.get_index()
                contact = view.get_contact()
                phone_book.change_contact(index, contact)
                view.show_message(texts.change_text)

        case '5' | 'del': # удалить контакт
            find_word = view.get_search()
            search = phone_book.find_contact(find_word)
            if len(search) < 1:
                print('Данные не обнаружены.')
            else:
                print(search)
                index = view.get_index()
                phone_book.del_contact(index)
                view.show_message(texts.del__text)

        case '6' | 'save': # сохранить файл
            phone_book.save_book()
            view.show_message(texts.save_text)

        case '7' | 'help' : # справка
            view.main_menu(texts.help)

        case '8' | 'exit': # выход
            exit()

        case _:
            view.main_menu(texts.help)
