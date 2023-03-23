def main_menu(text: str):
    menu = text.split('\n')
    for i, item in enumerate(menu):
        if i == 0:
            print(item)
        else:
            print(i, item)

def show_message(text: str):
    print(text)

def show_contacts(base: list):
    for i, contact in enumerate(base):
        print(f'{i+1}. {contact["name"]:<35}'
              f'{contact["number"]:<17}'
              f'{contact["comment"]:<20}')

def show_search(base: list):
    for contact in base:
        print(f'{contact["index"]}. {contact["name"]:<35}'
              f'{contact["number"]:<17}'
              f'{contact["comment"]:<20}')

def get_index():
    return int(input('Введите номер записи: '))

def get_search():
    return input('Введите данные для поиска: ').lower()

def get_contact():
    print('Введите данные или оставьте поле пустым, если нет изменений:')
    name = input('Введите имя: ')
    number = input('Введите телефон: ')
    comment = input('Введите комментарии: ')
    dict = {'name': name, 'number': number, 'comment': comment}
    return dict
