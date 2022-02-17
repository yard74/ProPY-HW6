documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

HELP = '''
Список доступных команд:
p - узнать имя человека по номеру документа
s - узнать номер полки, на которой находится документ
l - вывести список всех документов
a - добавить новый документ
d - удалить документ
m - переместить документ с одной полки на другую
as - добавить новую полку
ls - вывести список всех полок с документами
exit - завершить работу программы
'''


def get_doc_owner_name(docs, doc_number):
    for doc in docs:
        if doc_number == doc['number']:
            # print(doc['name'])
            return doc['name']
    else:
        return 'Человека с таким документом нет в системе.'


def get_shelf_number(shelves, doc_number):
    for key, value in shelves.items():
        if doc_number in value:
            # print(f'Документ находится на полке № {key}.')
            return key
    else:
        # print('Документ отсутствует в системе.')
        return 'Документ отсутствует в системе.'


def get_docs_list(docs):
    for doc in docs:
        # print(f'{doc["type"]} {doc["number"]} {doc["name"]}')
        return f'{doc["type"]} {doc["number"]} {doc["name"]}'


def put_new_doc(docs, shelves, doc_type, doc_number, doc_name, shelf_number):
    if shelf_number in shelves.keys():
        docs.append({"type": doc_type, "number": doc_number, "name": doc_name})
        for key, value in shelves.items():
            if shelf_number == key:
                value.append(doc_number)
                return 'Новый документ добавлен'
    else:
        # print('Полки с таким номером не существует. Документ не добавлен.')
        return 'Полки с таким номером не существует. Документ не добавлен.'


def delete_doc(docs, shelves, doc_number):
    for doc in docs:
        if doc['number'] == doc_number:
            docs.remove(doc)
    for shelf in shelves:
        if doc_number in shelves[shelf]:
            shelves[shelf].remove(doc_number)
            # print('Документ успешно удален.')
            return 'Документ успешно удален.'
    # print('Документа c таким номером не существует.')
    return 'Документа c таким номером не существует.'


def move_doc_to_shelf(shelves, doc_number, shelf_number):
    if shelf_number not in shelves:
        print(f'Полки с номером {shelf_number} не существует.')
        return
    for shelf, value in shelves.items():
        if doc_number in value:
            shelves[shelf_number] += [doc_number]
            value.remove(doc_number)
            print(f'Документ {doc_number} перемещен на полку с номером {shelf_number}.')
            return
    print('Документ не найден.')


def add_new_shelf(shelves, new_shelf):
    if new_shelf in shelves.keys():
        print(f'Полка с номером {new_shelf} уже существует.')
    else:
        shelves[new_shelf] = []
        print(f'Полка с номером {new_shelf} добавлена.')


def shelves_list(shelves):
    for key, value in shelves.items():
        if len(value) != 0:
            print(f'На полке № {key} находятся документы: {"; ".join(value)}.')
        else:
            print(f'На полке № {key} отсутствуют документы.')


def start_program():
    print('Для ознакомления со списком доступных команд введите HELP.')
    print()
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            doc_number = input('Введите номер документа: ')
            get_doc_owner_name(documents, doc_number)
        elif command == 's':
            doc_number = input('Введите номер документа: ')
            get_shelf_number(directories, doc_number)
        elif command == 'l':
            get_docs_list(documents)
        elif command == 'a':
            doc_type = input('Введите тип документа: ')
            doc_number = input('Введите номер документа: ')
            doc_name = input('Введите имя владельца документа: ')
            shelf_number = input('Укажите номер полки, на которую следует положить документ: ')
            put_new_doc(documents, directories, doc_type, doc_number, doc_name, shelf_number)
        elif command == 'd':
            doc_number = input('Введите номер документа: ')
            delete_doc(documents, directories, doc_number)
        elif command == 'm':
            doc_number = input('Введите номер документа: ')
            shelf_number = input('Введите номер полки, на которую следует переместить документ: ')
            move_doc_to_shelf(directories, doc_number, shelf_number)
        elif command == 'as':
            new_shelf_number = input('Введите номер для новой полки: ')
            add_new_shelf(directories, new_shelf_number)
        elif command == 'ls':
            shelves_list(directories)
        elif command.upper() == 'HELP':
            print(HELP)
        elif command == 'exit':
            print('Вы завершили работу. До свидания!')
            break
        else:
            print('Неизвестная команда! Воспользуйтесь справкой -> HELP')
            print()


if __name__ == '__main__':
    start_program()

