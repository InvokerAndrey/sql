"""
Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК.
Вывести: type, model, speed
"""
from queries.models import Laptop, PC
from django.db import connection, reset_queries
from django.db.models import Min


def run():
    result = Laptop.objects.values('model__type', 'model', 'speed').filter(speed__lt=PC.objects.aggregate(Min('speed'))['speed__min'])
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| type | model | speed |')
    print('_______________________')
    for item in result:
        print(f"| {item['model__type']} | {item['model']} | {item['speed']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT DISTINCT Product.type, Product.model, Laptop.speed FROM Laptop, Product
WHERE Laptop.model = Product.model 
AND Laptop.speed < (SELECT MIN(PC.speed) FROM PC)
"""

"""
Правильный результат:
type	model	speed
Laptop	1298	350
"""