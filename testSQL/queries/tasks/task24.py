"""
Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
"""
from queries.models import PC, Laptop, Printer, Product
from django.db import connection, reset_queries
from django.db.models import Max, Q


def run():
    max_printer = Printer.objects.aggregate(max_printer=Max('price'))
    max_laptop = Laptop.objects.aggregate(max_laptop=Max('price'))
    max_PC = PC.objects.aggregate(max_PC=Max('price'))
    max_price = max(max_printer['max_printer'], max_PC['max_PC'], max_laptop['max_laptop'])
    result = Product.objects.values('model').filter(Q(pc__price=max_price) | Q(laptop__price=max_price) | Q(printer__price=max_price))
    return result


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| model |')
    print(' _______')
    for item in result:
        print(f"| {item['model']} |")

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
Правильный результат:
model
1750
"""