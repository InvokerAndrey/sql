"""
Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
"""
from queries.models import PC
from django.db.models import Q


def run():
    result = PC.objects.values('model', 'speed', 'hd').filter((Q(cd='12x') | Q(cd='24x')) & Q(price__lt=600))
    return result


def print_result():
    result = run()
    print('| model | ram | screen |')
    print('__________________')
    for item in result:
        print(f"| {item['model']} | {item['speed']} | {item['hd']} |")

"""
SQL:
SELECT model, speed, hd FROM PC WHERE (cd = '12x' OR cd = '24x') AND price < 600
"""

"""
Правильный результат:
model	speed	hd
1232	500	    10.0
1232	450     8.0
1232	450	    10.0
1260	500	    10.0
"""