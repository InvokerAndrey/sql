"""
Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price
"""
from queries.models import Printer
from django.db import connection, reset_queries
from django.db.models import Min


def run():
    result = Printer.objects.values('model__maker', 'price').filter(price=Printer.objects.filter(color='y').aggregate(min_price=Min('price'))['min_price'], color='y')
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker | price |')
    print(' _______________')
    for item in result:
        print(f"| {item['model__maker']} | {item['price']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT DISTINCT Product.maker, Printer.price FROM Product, Printer
WHERE Product.model = Printer.model AND Printer.color = 'y' AND Printer.price = (SELECT MIN(price) FROM Printer WHERE color = 'y')
"""

"""
Правильный результат:
maker	price
D	270.0000
"""