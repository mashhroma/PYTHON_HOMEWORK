def main_menu(text: str):
    menu = text.split('\n')
    for i, item in enumerate(menu):
        if i == 0:
            print(item)
        else:
            print(i, item)

def show_message(text: str):
    print(text)

def get_index():
    return int(input('Введите номер записи: '))

def get_search():
    return input('Введите данные для поиска: ').lower()

def get_contact():
    print('Введите данные или оставьте поле пустым, если нет изменений:')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарии: ')
    dict = {'name': name, 'phone': phone, 'comment': comment}
    return dict