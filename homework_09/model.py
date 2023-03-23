phone_book = []
path = 'phone_base.txt'

def open_book():
    with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
    for contact in data:
        list = contact.replace('\n', '').split(';')
        dict = {'name': list[0], 'number': list[1], 'comment': list[2]}
        phone_book.append(dict)
    return phone_book

def save_book():
    data = []
    for contact in phone_book:
        data.append(f'{contact["name"]};{contact["number"]};{contact["comment"]}')
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def find_contact(find_text: str):
    search_result = []
    for i, contact in enumerate(phone_book):
        for_search = str(contact).lower()
        if find_text in for_search:
            contact['index'] = i+1
            search_result.append(contact)
    return search_result

def add_contact(contact: dict):
    phone_book.append(contact)
    return phone_book

def change_contact(index: int, contact: dict):
    phone_book[index-1] = {'name': contact.get('name') if contact.get('name') else phone_book[index-1].get('name'),
                           'number': contact.get('number') if contact.get('number') else phone_book[index-1].get('number'),
                           'comment': contact.get('comment') if contact.get('comment') else phone_book[index-1].get('comment')}
    return phone_book

def del_contact(index: int):
    phone_book.pop(index-1)
    return phone_book