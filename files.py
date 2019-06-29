#В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
# Задача №1
# Должен получится следующий словарь
#
    # cook_book = {
    #   'Омлет': [
    #     {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    #     {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    #     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    #     ],
    #   'Утка по-пекински': [
    #     {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    #     {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    #     {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    #     {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    #     ],
    #   'Запеченный картофель': [
    #     {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    #     {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    #     {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    #     ]
    #   }
# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
    # get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количетсва для блюда. Например, для такого вызова
#
    # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
    # {
    #   'Картофель': {'measure': 'кг', 'quantity': 2},
    #   'Молоко': {'measure': 'мл', 'quantity': 200},
    #   'Помидор': {'measure': 'шт', 'quantity': 8},
    #   'Сыр гауда': {'measure': 'г', 'quantity': 200},
    #   'Яйцо': {'measure': 'шт', 'quantity': 4},
    #   'Чеснок': {'measure': 'зубч', 'quantity': 6}
    # }
# Обратите внимание, что ингредиенты могут повторяться


with open('recipes.txt') as file:
    cook_book = {}
    for line in file:
        line = line.strip()
        cook_book.update({line: []})
        k = int(file.readline().strip())
        for _ in range(k):
            lst = file.readline().strip().split(' | ')
            dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
            cook_book[line].append(dict)
        file.readline()

# print(cook_book)

def view_cook_book(c_b):
    """
    Отображение списка рецептов блюд из файла.

    :param c_b:
    :return:
    """
    for key, value in c_b.items():
        print(f'\n {key}')
        for dct in value:
            string = dct['ingredient_name'] + ' - ' + dct['quantity'] + ' ' + dct['measure']
            print(f'{"    "}{string}')

# view_cook_book(cook_book)

def view_shopping_list(s_l):
    """
    Вывод списка ингредиентов для выбранных блюд с учетом количества человек.
    :param s_l:
    :return:
    """
    print('\nДля приготовления этих блюд пондобится:\n')
    index = 1
    for key, values in s_l.items():
        print(f"   {index}. {key} {values['quantity']} {values['measure']}")
        index += 1
    print('\n  Что-то из этого перечня можно будет найти на кухне, а остальное придется купить в магазине)))\n')

def get_shop_list_by_dishes(dishes, person_count):
    """
    Формирование списка необходимых ингредиетов с учетом введеных блюд и количества персон.
    :param dishes:
    :param person_count:
    :return:
    """
    shopping_list = {}
    for ingred in dishes:
        for ingr in cook_book[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    view_shopping_list(shopping_list)

# get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Фахитос', 'Жульен', 'Овощное рагу'], 5)

def input_ingredients():
    """
    Ввод списка жлаемых блюд и количества персон.
    :return:
    """
    try:
        lst = list(input('Введите через запятую желаемые блюда: ').split(', '))
        persons = int(input('Введите количество персон: '))
        get_shop_list_by_dishes(lst, persons)
    except Exception:
        print('Кажется Вы где-то ошиблись с вводом. Перепроверьте и введите заново, но без ошибок :)')

# input_ingredients()


def very_main():
    print('\n\nДобро пожаловать в список рецептов!'.upper())
    print('\n\nВам необходимо ввести номер действия, чтобы программа выполнила нужное действие: '
          '\n\n   1. Вывод рецептов.'
          '\n   2. Ввод нужных рецептов и количества человек. Программа вернет список необходимых ингредиентов.'
          '\n   9. Вывод этой справки.'
          '\n   0. Выйти из программы.')
    while True:
        prog = str(input('\n=========================================================================================='
                         '\n\n  номер действия: '.upper()))
        if prog == '1':
            view_cook_book(cook_book)
        elif prog == '2':
            input_ingredients()
        elif prog == '9':
            print('\n\nВам необходимо ввести номер действия, чтобы программа выполнила нужное действие: '
                  '\n\n   1. Вывод рецептов.'
                  '\n   2. Ввод нужных рецептов и количества человек. Программа вернет список необходимых ингредиентов.'
                  '\n   9. Вывод этой справки.'
                  '\n   0. Выйти из программы.')
        elif prog == '0':
            print('\n   Надеемся Вам очень понравилась наша программа!',
                  '\n   Вопросы и предложения присылайте по адресу: info@it-vi.ru',
                  '\n   Досвидания!'.upper())
            break
        else:
            print('\nТакой функционал программы пока не подвезли)))'
                  '\nЕсть предложения? Пишите по адресу: info@it-vi.ru')

if __name__ == '__main__':
    very_main()