"""
Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
Вывести: maker, максимальная цена.
"""
from queries.models import Product
from django.db import connection, reset_queries
from django.db.models import Max, Q


def run():
    result = Product.objects.values('maker').filter(type='PC').annotate(Max_price=Max('pc__price'))
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker | Max_price |')
    print(' ____________________')
    for item in result:
        print(f"| {item['maker']} | {item['Max_price']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT maker, MAX(price) FROM Product
JOIN PC ON Product.model = PC.model
GROUP BY maker
"""

"""
Правильный результат:

Maker	Max_price
A	    980.0000
B	    850.0000
E	    350.0000
"""