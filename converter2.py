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
            else: break

        while True:
            conversion_currency = input('Выберите валюту для конвертации: ')
            if conversion_currency not in CURRENCIES:
                print('Такой валюты нет в списке!')
                continue
            else:
                converted_amount = CURRENCIES.get(conversion_currency) / CURRENCIES.get(user_currency) * current_amount
                break

        return converted_amount, conversion_currency

def main():
    print('Добро пожаловать в конвертер валют')
    print('-'*34)

    print('''Наша программа поможет Вам конвертировать валюту.
    1. Введение имеющейся валюты
    2. Количество этой валюты
    3. Выбор валюты для конвертации''')
    print('-' * 34)

    print('Вам предложены следующие валюты: ')
    key_counter = 1
    for key in CURRENCIES:
        print(f'{key_counter}. {key}')
        key_counter += 1
    print('-' * 34)
    result = convert()
    print(f'Итого: {result[0]:.2f} {result[1]}')

if __name__ == '__main__':
    main()