"""
Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
"""
from queries.models import Laptop


def run():
    result = Laptop.objects.values('model', 'ram', 'screen').filter(price__gt=1000)
    return result


def print_result():
    result = run()
    print('| model | ram | screen |')
    print('__________________')
    for item in result:
        print(f"| {item['model']} | {item['ram']} | {item['screen']} |")

"""
SQL:
SELECT model, ram, screen FROM Laptop WHERE price > 1000
"""

"""
Правильный результат:
model	ram	screen
1750	128	14
1298	64	15
1752	128	14
"""