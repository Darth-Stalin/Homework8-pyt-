def menu():
    while True:
        print('Что вы хотите сделать?')
        user_choise = input('1 - Найти контакт\n2 - Добавить контакт\n3 - Удалить контакт\n4 - Изменить контакт\n5 - Посмотреть все контакты\n6 - Импортировать данные\n0 - Выйти из приложения\n')
        print()

        if user_choise == '1':
            contact_list = read_file()
            find_contact(contact_list)
        elif user_choise == '2':
            add_contact()
        elif user_choise == '3':
            delete_contact()
        elif user_choise == '4':
            change_contact()
        elif user_choise == '5':
            show_contact()
        elif user_choise == '6':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, 'phonebook\data.txt')
        elif user_choise == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно набрана команда!')
            print()
            continue

# Видим список в формате ФИО номер тел.
def read_file():
    with open('phonebook\data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list
print(read_file())

# Условия поиска контакта
def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по отчеству\n4 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите отчество для поиска: ')
        print()
    elif search_field == '4':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value

# Поиск контакта
def find_contact(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print(found_contacts)
    print()

# То что мы вносим в тел. книгу
def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, second_name, phone_number

# Добавление контакта
def add_contact(data):
    info = ' '.join(get_new_number())
    with open(data, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
    
# Чтение как список
def read_file_to_list():
    with open('phonebook\data.txt', 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

# Поиск, чтобы изменить
def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()

# Удаление контакта
def delete_contact():
    contact_list = read_file_to_list()
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open('phonebook\data.txt', 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Изменение контакта
def change_contact():
    contact_list = read_file_to_list()
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите отчество: ')
    elif field == '4':
        number_to_change[3] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open('phonebook\data.txt', 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

# Сортировка списка по алфавиту
def show_contact():
    list_of_contacts = sorted(read_file(), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts

# И вывод на печать
def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

# Импортирование
def import_data(file_to_add, data):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open('phonebook\data.txt', 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


if __name__ == '__main__':
    file = 'phonebook\data.txt'
    menu()