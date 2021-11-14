"""
Найдите производителей, которые производили бы как ПК
со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц.
Вывести: Maker
"""
from queries.models import Product
from django.db import connection, reset_queries


def run():
    pc = Product.objects.values('maker').filter(pc__speed__gte=750).distinct()
    laptop = Product.objects.values('maker').filter(laptop__speed__gte=750).distinct()
    return pc.intersection(laptop)


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| maker |')
    print(' _______')
    for item in result:
        print(f"| {item['maker']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
SQL:
SELECT maker FROM Product 
JOIN PC ON PC.model = Product.model
WHERE PC.speed >= 750
INTERSECT
SELECT maker FROM Product
JOIN Laptop ON Laptop.model = Product.model
WHERE Laptop.speed >= 750
"""

"""
Правильный результат:

maker
A
B
"""