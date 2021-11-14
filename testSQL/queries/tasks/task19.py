"""
Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов.
Вывести: maker, средний размер экрана.
"""
from queries.models import Product
from django.db import connection, reset_queries
from django.db.models import Avg


def run():
    result = Product.objects.values('maker').filter(type='Laptop').distinct().annotate(avg_screen=Avg('laptop__screen')).values('maker', 'avg_screen')
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker | avg_screen |')
    print(' ____________________')
    for item in result:
        print(f"| {item['maker']} | {item['avg_screen']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT maker, AVG(screen) FROM Laptop
JOIN Product ON Product.model = Laptop.model
GROUP BY maker
"""

"""
Правильный результат:
maker   avg_screen	
A	    13
B	    14
C	    12
"""