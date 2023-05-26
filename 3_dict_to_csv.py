import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """




    with open('users.csv', 'r', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
