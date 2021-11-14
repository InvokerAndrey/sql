from django.db import models

"""
Схема БД состоит из четырех таблиц:
Product(maker, model, type)
PC(code, model, speed, ram, hd, cd, price)
Laptop(code, model, speed, ram, hd, price, screen)
Printer(code, model, color, type, price)
Таблица Product представляет производителя (maker), номер модели (model)
и тип ('PC' - ПК, 'Laptop' - ПК-блокнот или 'Printer' - принтер). Предполагается, что номера моделей в таблице Product
уникальны для всех производителей и типов продуктов. В таблице PC для каждого ПК, однозначно определяемого
уникальным кодом – code, указаны модель – model (внешний ключ к таблице Product), скорость - speed (процессора в мегагерцах),
объем памяти - ram (в мегабайтах), размер диска - hd (в гигабайтах), скорость считывающего устройства - cd (например, '4x')
и цена - price. Таблица Laptop аналогична таблице РС за исключением того, что вместо скорости CD содержит
размер экрана -screen (в дюймах). В таблице Printer для каждой модели принтера указывается, является ли он
цветным - color ('y', если цветной), тип принтера - type (лазерный – 'Laser', струйный – 'Jet' или матричный – 'Matrix')
и цена - price.
"""

class Product(models.Model):
    maker = models.CharField(max_length=10)
    model = models.IntegerField(primary_key = True, max_length=10, unique=True)
    type = models.CharField(max_length=10)

    def __str__(self):
        return str(self.model)


class PC(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    speed = models.IntegerField(max_length=10)
    ram = models.IntegerField(max_length=10)
    hd = models.IntegerField(max_length=10)
    cd = models.CharField(max_length=10)
    price = models.IntegerField(max_length=10)


class Laptop(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    speed = models.IntegerField(max_length=10)
    ram = models.IntegerField(max_length=10)
    hd = models.IntegerField(max_length=10)
    screen = models.CharField(max_length=10)
    price = models.IntegerField(max_length=10)


class Printer(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    price = models.IntegerField(max_length=10)
