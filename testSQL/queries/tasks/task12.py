"""
Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол.
"""
from queries.models import Laptop
from django.db import connection, reset_queries
from django.db.models import Avg


def run():
    result = Laptop.objects.filter(price__gt=1000).aggregate(avg_speed=Avg('speed'))
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| avg_speed |')
    print('____________')
    print(f"| {result['avg_speed']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT AVG(speed) FROM Laptop WHERE price > 1000
"""

"""
Правильный результат:
avg_speed
700
"""