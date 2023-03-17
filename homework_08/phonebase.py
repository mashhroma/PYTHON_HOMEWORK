def BASE_OPEN(file):
    with open(file, 'r', encoding='UTF-8') as data:
        list = [line.replace('\n', '') for line in data]         
    return list


def SAVE_BASE(file, list):
    with open(file, 'w', encoding='UTF-8') as new_data:
        for item in list:
            new_data.writelines(f'{item}\n')
    return new_data


def SHOW_BASE(file):
    with open(file, 'r', encoding='UTF-8') as data:
        print(*data, sep='')


def FIND_CONTACT(file, find_info):
    result =''
    with open(file, 'r', encoding='UTF-8') as data:
        for line in data:
            if find_info.lower() in line.lower():
                result += line
        if len(result) < 1:
            result = 'Данных в справочнике нет.'
    return result


def ADD_CONTACT(list, add_info):
    list.append(add_info)
    return list


def FIND_INDEX(list, find_info):
    find_list =[]
    for i, item in enumerate(list):
        if find_info.lower() in item.lower():
            find_list.append(i)
    return find_list
