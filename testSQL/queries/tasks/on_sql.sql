1. Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
SELECT model, speed, hd FROM PC WHERE price < 500


2. Найдите производителей принтеров. Вывести: maker
SELECT DISTINCT maker FROM Product WHERE type = 'PC'


3. Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
SELECT model, ram, screen FROM Laptop WHERE price > 1000


4. Найдите все записи таблицы Printer для цветных принтеров.
SELECT * FROM Printer WHERE color = 'y'


5. Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
SELECT model, speed, hd FROM PC WHERE cd IN ('12x', '24x') AND price < 600


6. Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
SELECT DISTINCT maker, speed FROM Product
JOIN Laptop ON Product.model = Laptop.model
WHERE Laptop.hd >= 10


7. Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
SELECT Product.model, price FROM Product
JOIN PC ON Product.model = PC.model
WHERE Product.maker = 'B'
UNION
SELECT Product.model, price FROM Product
JOIN Laptop ON Product.model = Laptop.model
WHERE Product.maker = 'B'
UNION
SELECT Product.model, price FROM Product
JOIN Printer ON Product.model = Printer.model
WHERE Product.maker = 'B'


8. Найдите производителя, выпускающего ПК, но не ПК-блокноты.
SELECT maker FROM Product
WHERE type = 'PC'
EXCEPT
SELECT maker FROM Product
WHERE type = 'Laptop'


9. Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
SELECT DISTINCT maker FROM Product
JOIN PC ON Product.model = PC.model
WHERE speed >= 450


10. Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
SELECT model, price FROM Printer
WHERE price = (SELECT MAX(price) FROM Printer)


11. Найдите среднюю скорость ПК.
SELECT AVG(speed) FROM PC


12. Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол.
SELECT AVG(speed) FROM Laptop
WHERE price > 1000


13. Найдите среднюю скорость ПК, выпущенных производителем A.
SELECT AVG(speed) FROM PC
JOIN Product ON Product.model = PC.model
WHERE maker = 'A'


15. Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
SELECT hd FROM PC
GROUP BY hd HAVING COUNT(hd) >=2


16. Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i),
Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM.


17. Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК. Вывести: type, model, speed
SELECT DISTINCT type, Laptop.model, Laptop.speed FROM Laptop
JOIN Product ON Product.model = Laptop.model
WHERE Laptop.speed < (SELECT MIN(PC.speed) FROM PC)


18. Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price
SELECT DISTINCT maker, price FROM Product
JOIN Printer ON Product.model = Printer.model
WHERE color = 'y' AND price = (SELECT MIN(price) FROM Printer WHERE color = 'y')


19. Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов.
Вывести: maker, средний размер экрана.
SELECT maker, AVG(screen) FROM Product
JOIN Laptop ON Product.model = Laptop.model
GROUP BY maker


20. Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.
SELECT maker, COUNT(model) FROM Product
WHERE type = 'PC'
GROUP BY maker HAVING COUNT(model) >= 3


21. Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
Вывести: maker, максимальная цена.
SELECT maker, MAX(price) FROM Product
JOIN PC ON Product.model = PC.model
GROUP BY maker


22. Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена.
SELECT speed, AVG(price) FROM PC
WHERE speed > 600
GROUP BY speed


23. Найдите производителей, которые производили бы как ПК со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц.
Вывести: Maker
SELECT maker FROM Product
JOIN PC ON Product.model = PC.model
WHERE PC.speed >= 750
INTERSECT
SELECT maker FROM Product
JOIN Laptop ON Product.model = Laptop.model
WHERE Laptop.speed >= 750


24. Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
WITH max_prices AS (
SELECT MAX(price) as p FROM PC
UNION ALL
SELECT MAX(price) as p FROM Laptop
UNION ALL
SELECT MAX(price) as p FROM Printer
)
SELECT model FROM PC WHERE price = (SELECT MAX(p) as max_p FROM max_prices)
UNION
SELECT model FROM Laptop WHERE price = (SELECT MAX(p) as max_p FROM max_prices)
UNION
SELECT model FROM Printer WHERE price = (SELECT MAX(p) as max_p FROM max_prices)


25. Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM.
Вывести: Maker
SELECT maker FROM Product
JOIN PC ON Product.model = PC.model



from django.db.models import Avg
Offer.objects.values('price').aggregate(max_price=Max('price'))[:5]