import texts
import view
import model

view.main_menu(texts.help)

while True:
    choice = input('Ваш выбор (для справки - help): ').lower()
    match choice:
        case '1' | 'open': # открыть файл
            model.open_book()
            view.show_message(texts.open_text)
        case '2' | 'save': # сохранить файл
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                model.save_book()
                view.show_message(texts.save_text)
        case '3' | 'show': # посмотреть контакты
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                view.show_contacts(model.phone_book)
        case '4' | 'find': # найти контакт
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                find_word = view.get_search()
                search = model.find_contact(find_word)
                if len(search) < 1:
                    print('Данные не обнаружены.')
                else:
                    view.show_search(search)
        case '5' | 'add': # добавить контакт
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                new_contact = view.get_contact()
                model.add_contact(new_contact)
                view.show_message(texts.add_text)
        case '6' | 'change': # изменить контакт
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                find_word = view.get_search()
                search = model.find_contact(find_word)
                if len(search) < 1:
                    print('Данные не обнаружены.')
                else:
                    view.show_search(search)
                    index = view.get_index()
                    change_contact = view.get_contact()
                    model.change_contact(index, change_contact)
                    view.show_message(texts.change_text)
        case '7' | 'del': # удалить контакт
            if len(model.phone_book)<1:
                print('Необходимо вначале открыть книгу: команда 1 или open')
            else:
                find_word = view.get_search()
                search = model.find_contact(find_word)
                if len(search) < 1:
                    print('Данные не обнаружены.')
                else:
                    view.show_search(search)
                    index = view.get_index()
                    model.del_contact(index)
                    view.show_message(texts.del__text)
        case '8' | 'help' : # справка
            view.main_menu(texts.help)
        case '9' | 'exit': # выход
            exit()
        case _:
            view.main_menu(texts.help)
