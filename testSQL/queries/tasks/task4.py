"""
Найдите все записи таблицы Printer для цветных принтеров.
"""
from queries.models import Printer


def run():
    result = Printer.objects.filter(color='y')
    return result


def print_result():
    result = run()
    print('| code | model | color | type | price |')
    print('__________________')
    for item in result:
        print(f"| {item.code} | {item.model} | {item.color} | {item.type} | {item.price} |")

"""
SQL:
SELECT * FROM Printer WHERE color='y'
"""

"""
Правильный результат:
code	model	color	type	price
3	    1434	y	    Jet	    290.0000
2	    1433	y	    Jet	    270.0000
"""