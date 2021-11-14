"""
Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
"""
from queries.models import Printer
from django.db import connection, reset_queries
from django.db.models import Max, F


def run():
    max_price = Printer.objects.aggregate(max_price=Max('price'))
    result = Printer.objects.values('model', 'price').annotate(max_price=Max('price')).filter(price=max_price['max_price'])
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| model | price |')
    print('________________')
    for item in result:
        print(f"| {item['model']} | {item['price']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT model, price FROM Printer
WHERE price = (SELECT MAX(price) FROM Printer)
"""

"""
Правильный результат:
model	price
1288	400.0000
1276	400.0000
"""