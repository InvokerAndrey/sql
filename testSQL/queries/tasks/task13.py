"""
Найдите среднюю скорость ПК, выпущенных производителем A.
"""
from queries.models import PC
from django.db import connection, reset_queries
from django.db.models import Avg


def run():
    result = PC.objects.filter(model__maker='A').aggregate(avg_speed=Avg('speed'))
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
SELECT AVG(speed) FROM PC JOIN Product ON Product.model=PC.model
WHERE Product.maker='A'
"""

"""
Правильный результат:
avg_speed
606
"""