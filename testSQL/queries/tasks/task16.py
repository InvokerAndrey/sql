"""
Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз,
т.е. (i,j), но не (j,i), Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM.
"""
from queries.models import PC
from django.db import connection, reset_queries
from django.db.models import Count


def run():
    pass


def print_result():
    reset_queries()
    start_queries = len(connection.queries)

    result = run()

    print('| model | model | speed | ram |')
    print('_______________________________')
    for item in result:
        pass

    end_queries = len(connection.queries)
    print('Number of queries:', end_queries - start_queries)

"""
Правильный результат:
model	model	speed	ram
1233	1121	750	    128
1233	1232	500	    64
1260	1232	500	    32
""" 