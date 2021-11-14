"""
Найдите производителя, выпускающего ПК, но не ПК-блокноты.
"""
from queries.models import Product
from django.db import connection, reset_queries


def run():
    result = Product.objects.values('maker').filter(type__in=['PC']).distinct()
    to_except = Product.objects.values('maker').filter(type__in=['Laptop']).distinct()
    return result.difference(to_except)


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
SELECT DISTINCT maker FROM Product WHERE type in ('PC')
EXCEPT
SELECT DISTINCT maker FROM Product WHERE type in ('Laptop')
"""

"""
Правильный результат:
maker
E
"""