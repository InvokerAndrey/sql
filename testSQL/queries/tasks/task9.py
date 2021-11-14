"""
Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
"""
from queries.models import Product
from django.db import connection, reset_queries


def run():
    result = Product.objects.values('maker').filter(pc__speed__gte=450).distinct()
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker |')
    print('________________')
    for item in result:
        print(f"| {item['maker']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT DISTINCT maker FROM Product JOIN PC ON PC.model = Product.model
WHERE PC.speed >= 450
"""

"""
Правильный результат:
maker
A
B
E
"""