"""
Найдите производителей принтеров. Вывести: maker
"""
from queries.models import Product


def run():
    result = Product.objects.values('maker').filter(type='Printer').distinct()
    return result


def print_result():
    result = run()
    print('| maker |')
    print('__________________')
    for item in result:
        print(f"| {item['maker']} |")

"""
SQL:
SELECT DISTINCT maker FROM Product WHERE type = 'Printer'
"""

"""
Правильный результат:
maker
A
D
E
"""