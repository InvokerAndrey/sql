"""
Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью.
Вывести: speed, средняя цена.
"""
from queries.models import PC
from django.db import connection, reset_queries
from django.db.models import Avg


def run():
    result = PC.objects.values('speed').filter(speed__gt=600).annotate(Avg_price=Avg('price'))
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| speed | Avg_price |')
    print(' ____________________')
    for item in result:
        print(f"| {item['speed']} | {item['Avg_price']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT speed, AVG(price) FROM PC
WHERE speed > 600
GROUP BY speed
"""

"""
Правильный результат:

speed	Avg_price
750	    900.0000
800	    970.0000
900	    980.0000
"""