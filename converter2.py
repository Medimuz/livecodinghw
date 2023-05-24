from onlinerequests import CURRENCIES


def convert():
    while True:
        user_currency = input("Введите имеющуюся валюту: ")
        if user_currency not in CURRENCIES:
            print('Такой валюты нет в списке!')
            continue

        while True:
            current_amount = float(input('Введите имеющуся сумму: '))
            if current_amount <= 0:
                print('Число должно быть больше 0!')
                continue
            else:
                break

        while True:
            conversion_currency = input('Выберите валюту для конвертации: ')
            if conversion_currency not in CURRENCIES:
                print('Такой валюты нет в списке!')
                continue
            else:
                converted_amount = CURRENCIES.get(conversion_currency) / CURRENCIES.get(user_currency) * current_amount
                break
        print(f'Итого: {converted_amount:.2f} {conversion_currency}')
        break


def continuation():
    """Запрос пользователю на продолжение работы"""
    while True:
        repeat = input('Желаете продолжить? Напишите "да" или "нет": ').lower()
        if repeat not in ["да", "нет"]:
            print('Введите "да" или "нет".')
            continue
        elif repeat == "да":
            main()
        print('До свидания!')
        break


def greetings():
    """Приветствие"""
    print('Добро пожаловать в конвертер валют')
    print('-' * 34)

    print('''Наша программа поможет Вам конвертировать валюту.
        1. Введение имеющейся валюты
        2. Количество этой валюты
        3. Выбор валюты для конвертации''')
    print('-' * 34)


def currencies_to_choose():
    """Вывод списка достуаных валют"""
    print('Вам предложены следующие валюты: ')
    key_counter = 1
    for key in CURRENCIES:
        print(f'{key_counter}. {key}')
        key_counter += 1
    print('-' * 34)


def main():
    greetings()
    currencies_to_choose()
    convert()
    continuation()


if __name__ == '__main__':
    main()
