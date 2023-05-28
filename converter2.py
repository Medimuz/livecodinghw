from onlinerequests import CURRENCIES


def convert_currecies(currency, amount):
    """Функиия конвертации"""
    while True:
        conversion_currency = input('Выберите валюту для конвертации: ')
        if conversion_currency in CURRENCIES:
            converted_amount = CURRENCIES.get(conversion_currency) / CURRENCIES.get(currency) * amount
            print(f'Итого: {converted_amount:.2f} {conversion_currency}')
            break
        else:
            print('Такой валюты нет в списке!')
    request_continuation()


def users_input():
    while True:
        user_currency = input("Введите имеющуюся валюту: ")
        if user_currency in CURRENCIES:
            break
        else:
            print('Такой валюты нет в списке!')
    while True:
        try:
            current_amount = float(input('Введите имеющуся сумму: '))
            if current_amount > 0:
                break
            else:
                print('Число должно быть больше 0!')
        except:
            print('Нужно ввести число!')
    convert_currecies(user_currency, current_amount)


def request_continuation():
    """Запрос пользователю на продолжение работы"""
    while True:
        repeat = input('Желаете продолжить? Напишите "да" или "нет": ').lower()
        if repeat == 'да':
            users_input()
            break
        elif repeat == 'нет':
            print('До свидания!')
            break
        else:
            print('Введите "да" или "нет"')


def greetings():
    """Приветствие"""
    print('Добро пожаловать в конвертер валют')
    print('-' * 34)

    print('''Наша программа поможет Вам конвертировать валюту.
        1. Введение имеющейся валюты
        2. Количество этой валюты
        3. Выбор валюты для конвертации''')
    print('-' * 34)
    currencies_to_choose()


def currencies_to_choose():
    """Вывод списка достуаных валют"""
    print('Вам предложены следующие валюты: ')
    key_counter = 1
    for key in CURRENCIES:
        print(f'{key_counter}. {key}')
        key_counter += 1
    print('-' * 34)
    users_input()


if __name__ == '__main__':
    greetings()