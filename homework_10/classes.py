class Contact:
    def __init__(self, index: int, name: str, phone: str, comment: str):
        self.index = index
        self.name = name
        self.phone = phone
        self.comment = comment
    
    def to_str(self):
        return f'{self.index};{self.name};{self.phone};{self.comment}'

    def to_str_save(self):
        return f'{self.name};{self.phone};{self.comment}'

    def __str__(self) -> str:
        return f'{self.index: <3} | {self.name: <35} |  {self.phone: <17}  |  {self.comment: <20}'


class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_list = []
        self.open_book()

    def open_book(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for index, contact in enumerate(data):
            new_contact = contact.strip().split(';')
            new_contact.insert(0, index+1)
            self.phone_list.append(Contact(*new_contact))

    def find_contact(self, find: str):
        search_result = []
        for contact in self.phone_list:
            if find in contact.to_str().lower():
                search_result.append(f'{contact}')
        return '\n'.join(search_result)

    def add_contact(self, contact: dict):
        index = len(self.phone_list)+1
        name = contact['name']
        phone = contact['phone']
        comment = contact['comment']
        self.phone_list.append(Contact(index, name, phone, comment))

    def change_contact(self, index: int, contact: dict):
        name = contact.get('name') if contact.get('name') != '' else self.phone_list[index-1].name
        phone = contact.get('phone') if contact.get('phone') != '' else self.phone_list[index-1].phone
        comment = contact.get('comment') if contact.get('comment') != '' else self.phone_list[index-1].comment
        self.phone_list[index-1] = Contact(index, name, phone, comment)

    def del_contact(self, index: int):
        if index < len(self.phone_list):
            for i in range(index-1, len(self.phone_list)):
                self.phone_list[i].index -= 1
        self.phone_list.pop(index-1)

    def save_book(self):
        data = []
        for contact in self.phone_list:
            data.append(contact.to_str_save())
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def to_str_save(self):
        return f'{self.name};{self.phone};{self.comment}'

    def __str__(self) -> str:
        result = ''
        i = 0
        for contact in self.phone_list:
            i += 1
            result += f'{contact}\n'
        return result[:-2]
