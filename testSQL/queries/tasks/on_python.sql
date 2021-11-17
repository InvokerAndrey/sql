1. Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
PC.objects.values('model', 'speed', 'hd').filter(price__lt=500)


2. Найдите производителей принтеров. Вывести: maker
Product.objects.values('maker').filter(type='Printer').distinct()


3. Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
Laptop.objects.values('model', 'ram', 'screen').filter(price__gt=1000)


4. Найдите все записи таблицы Printer для цветных принтеров.
Printer.objects.filter(color='y')


5. Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
PC.objects.values('model', 'speed', 'hd').filter(cd__in=['12x', '24x'], price__lt=600)


6. Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
Laptop.objects.values('model__maker', 'speed').filter(hd__gte=10)


7. Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
pcs = PC.objects.values('model', 'price').filter(model__maker='B').distinct()
laptops = Laptop.objects.values('model', 'price').filter(model__maker='B').distinct()
printers = Printer.objects.values('model', 'price').filter(model__maker='B').distinct()
printers.union(pcs, laptops)



8. Найдите производителя, выпускающего ПК, но не ПК-блокноты.
pcs = Product.objects.values('maker').filter(type='PC').distinct()
to_trim = Product.objects.filter(type='Laptop').distinct()
pcs.difference(to_trim)


9. Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
Product.objects.values('maker').filter(pc__speed__gte=450).distinct()


10. Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
Printer.objects.values('model', 'price').filter(price=Printer.objects.aggregate(max_price=Max('price'))['max_price'])


11. Найдите среднюю скорость ПК.
PC.objects.aggregate(Avg('speed'))


12. Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол.
Laptop.objects.filter(price__gt=1000).aggregate(Avg('speed'))


13. Найдите среднюю скорость ПК, выпущенных производителем A.
PC.objects.filter(model__maker='A').aggregate(Avg('speed'))


15. Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
            group by
PC.objects.values('hd').annotate(Count('hd')).filter(hd__count__gte=2).values('hd')


16. Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i),
Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM.


17. Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК. Вывести: type, model, speed
Product.objects.values('type', 'model', 'laptop__speed').filter(laptop__speed__lt=PC.objects.aggregate(min_speed=Min('speed'))['min_speed'])


18. Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price



19. Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов.
Вывести: maker, средний размер экрана.



20. Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.



21. Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
Вывести: maker, максимальная цена.



22. Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена.



23. Найдите производителей, которые производили бы как ПК со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц.
Вывести: Maker



24. Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.


25. Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM.
Вывести: Maker
