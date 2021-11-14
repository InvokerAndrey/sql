"""
Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
"""
from queries.models import PC
from django.db import connection, reset_queries
from django.db.models import Count


def run():
    result = PC.objects.values('hd').annotate(Count('hd')).filter(hd__count__gte=2)
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| hd |')
    print('_____')
    for item in result:
        print(f"| {item['hd']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT HD FROM PC GROUP BY HD HAVING COUNT(HD) >= 2
"""

"""
Правильный результат:
HD
5.0
8.0
10.0
14.0
20.0
"""