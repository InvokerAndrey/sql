"""
Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
"""
from queries.models import Product
from django.db import connection, reset_queries
from django.db.models import F


def run():
    laptops = Product.objects.annotate(price=F('laptop__price')).values('model', 'price').filter(maker='B').exclude(price=None).distinct()
    PCs = Product.objects.annotate(price=F('pc__price')).values('model', 'pc__price').filter(maker='B').exclude(pc__price=None).distinct()
    printers = Product.objects.annotate(price=F('printer__price')).values('model', 'printer__price').filter(maker='B').exclude(printer__price=None).distinct()
    result = laptops.union(PCs, printers)
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
SELECT DISTINCT PC.model, PC.price FROM PC JOIN Product
ON PC.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT DISTINCT Laptop.model, Laptop.price FROM Laptop JOIN Product
ON Laptop.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT DISTINCT Printer.model, Printer.price FROM Printer JOIN Product
ON Printer.model = Product.model
WHERE Product.maker = 'B'
"""

"""
Правильный результат:
model	price
1121	850.0000
1750	1200.0000
"""