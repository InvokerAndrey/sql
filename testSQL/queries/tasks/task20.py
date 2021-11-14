"""
Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.
"""
from queries.models import Product
from django.db import connection, reset_queries
from django.db.models import Count


def run():
    result = Product.objects.values('maker').annotate(PC_count=Count('model')).filter(type='PC', PC_count__gte=3)
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker | PC_count |')
    print(' ____________________')
    for item in result:
        print(f"| {item['maker']} | {item['PC_count']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT maker, COUNT(model) FROM Product
WHERE type = 'PC'
GROUP BY maker HAVING COUNT(model) >= 3
"""

"""
Правильный результат:

maker   PC_count	
E	    3
"""