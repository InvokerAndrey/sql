"""
Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
"""

from queries.models import PC


def run():
    result = PC.objects.values('model', 'speed', 'hd').filter(price__lt=500)
    return result


def print_result():
    result = run()
    print('model | speed | hd')
    print('__________________')
    for item in result:
        print(f"{item['model']} | {item['speed']} | {item['hd']}")

"""
SQL:
SELECT model, speed, hd FROM PC WHERE price < 500
"""

"""
Правильный результат:
model	speed	hd
1232	500	    10.0
1232	450	    8.0
1232	450	    10.0
1260	500	    10.0
"""