def choose_action():
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Найти контакт\n2 - Добавить контакт\n\
3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':

            find_number()
        elif user_choice == '2':
            add_phone_number()
        elif user_choice == '3':
            change_phone_number()
        elif user_choice == '4':
            delete_contact()
        elif user_choice == '5':
            contact_list = read_csv()
            print_list(contact_list)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

# функция списка словарей с ключами (фамилия, имя)
def read_csv():
    data = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('phone_book.txt', 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    print()
    return data

# функция списка справочника
def read_file_to_list():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split(','))
    return contact_list

# функция выбора параметра (ключа)по которому ищем абонента
def search_to_modify(contact_list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    print()
    
# функция печатает список абонентов
def print_list(contact_list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

# функция параметров для поиска абонента
def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value

# функция ищет абонента по ключам (фамилия, имя)
def find_number():
    contact_list = read_csv()
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Телефон'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_list(found_contacts)
    print()

# функция для добавления нового абонента по ключам(фамилия,имя)
def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description= input('Введите краткое описание: ')
    return last_name, first_name, phone_number, description
# функция добавляет нового абонента
def add_phone_number():
    info = ','.join(get_new_number())
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')

# функция удаляет абонента
def delete_contact():
    contact_list = read_file_to_list()
    number_to_change = search_to_modify(contact_list)
    if number_to_change==None:
        print('Контакт не найден!')
    else:
        contact_list.remove(number_to_change)
        with open('phone_book.txt', 'w', encoding='utf-8') as file:
            for contact in contact_list:
                line = ','.join(contact)
                file.write(line)

# функция изменяет данные абонента
def change_phone_number():
    contact_list = read_file_to_list()
    number_to_change = search_to_modify(contact_list)
    if number_to_change==None:
        print('Контакт не найден!')
    else:
        contact_list.remove(number_to_change)
        print('Какое поле вы хотите изменить?')
        field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
        if field == '1':
            number_to_change[0] = input('Введите фамилию: ')
        elif field == '2':
            number_to_change[1] = input('Введите имя: ')
        elif field == '3':
            number_to_change[2] = input('Введите номер телефона: ')
        contact_list.append(number_to_change)
        with open('phone_book.txt', 'w', encoding='utf-8') as file:
            for contact in contact_list:
                line = ','.join(contact)
                file.writelines(line)

choose_action()


'''
Викторов,Николай,+7983,глупый студент
Иванов,Иван,111,описание
Петров,Петр,222,описание
Сидоров,Сергей,333,описание
'''
