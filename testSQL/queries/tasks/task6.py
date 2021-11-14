"""
Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт,
найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
"""
from queries.models import Product, Laptop
from django.db import connection, reset_queries


def run():
    result = Laptop.objects.values('model__maker', 'speed').filter(hd__gte=10).distinct()
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker | speed |')
    print('________________')
    for item in result:
        print(f"| {item['model__maker']} | {item['speed']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT DISTINCT Product.maker, Laptop.speed FROM Laptop INNER JOIN Product
ON Laptop.model = Product.model WHERE Laptop.hd >= 10
"""

"""
Правильный результат:
maker	speed
A	    450
A	    600
A	    750
B	    750
"""