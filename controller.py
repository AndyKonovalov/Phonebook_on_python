import functional

def choice_todo():
    print('Добро пожаловать!')
    while True:
        print("""Выберите действие:
        1 - Добавить контакт
        2 - Показать контакты
        3 - Поиск контакта.
        0 - Выйти из справочника.""")
        ch = input("Введите цифру: ")
        if ch == '1':
            functional.import_data(functional.input_data())
        elif ch == '2':
            data = functional.export_data()
            functional.print_data(data)
        elif ch == '3':
            word = input("Введите данные для поиска: ")
            data = functional.export_data()
            item = functional.search_data(word, data)
            if item != None:
                print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
                print("-"*85)
                print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            break