from .models import *


def insert_into_product():
    product = Product.objects.create(maker='A', model=1232, type='PC')
    product.save()

    product = Product.objects.create(maker='A', model=1233, type='PC')
    product.save()

    product = Product.objects.create(maker='A', model=1276, type='Printer')
    product.save()

    product = Product.objects.create(maker='A', model=1298, type='Laptop')
    product.save()

    product = Product.objects.create(maker='A', model=1401, type='Printer')
    product.save()

    product = Product.objects.create(maker='A', model=1408, type='Printer')
    product.save()

    product = Product.objects.create(maker='A', model=1752, type='Laptop')
    product.save()

    product = Product.objects.create(maker='B', model=1121, type='PC')
    product.save()

    product = Product.objects.create(maker='B', model=1750, type='Laptop')
    product.save()

    product = Product.objects.create(maker='C', model=1321, type='Laptop')
    product.save()

    product = Product.objects.create(maker='D', model=1288, type='Printer')
    product.save()

    product = Product.objects.create(maker='D', model=1433, type='Printer')
    product.save()

    product = Product.objects.create(maker='E', model=1260, type='PC')
    product.save()

    product = Product.objects.create(maker='E', model=1434, type='Printer')
    product.save()

    product = Product.objects.create(maker='E', model=2112, type='PC')
    product.save()

    product = Product.objects.create(maker='E', model=2113, type='PC')
    product.save()


def insert_into_PC():
    pc = PC.objects.create(code=1, model=Product.objects.get(model=1232), speed=500, ram=64, hd=5, cd='12x', price=600)
    pc.save()

    pc = PC.objects.create(code=2, model=Product.objects.get(model=1121), speed=750, ram=128, hd=14, cd='40x', price=850)
    pc.save()

    pc = PC.objects.create(code=3, model=Product.objects.get(model=1233), speed=500, ram=64, hd=5, cd='12x', price=600)
    pc.save()

    pc = PC.objects.create(code=4, model=Product.objects.get(model=1121), speed=600, ram=128, hd=14, cd='40x', price=850)
    pc.save()

    pc = PC.objects.create(code=5, model=Product.objects.get(model=1121), speed=600, ram=128, hd=8, cd='40x', price=850)
    pc.save()

    pc = PC.objects.create(code=6, model=Product.objects.get(model=1233), speed=750, ram=128, hd=20, cd='50x', price=950)
    pc.save()

    pc = PC.objects.create(code=7, model=Product.objects.get(model=1232), speed=500, ram=32, hd=10, cd='12x', price=400)
    pc.save()

    pc = PC.objects.create(code=8, model=Product.objects.get(model=1232), speed=450, ram=64, hd=8, cd='24x', price=350)
    pc.save()

    pc = PC.objects.create(code=9, model=Product.objects.get(model=1232), speed=450, ram=32, hd=10, cd='24x', price=350)
    pc.save()

    pc = PC.objects.create(code=10, model=Product.objects.get(model=1260), speed=500, ram=32, hd=10, cd='12x', price=350)
    pc.save()

    pc = PC.objects.create(code=11, model=Product.objects.get(model=1233), speed=900, ram=128, hd=40, cd='40x', price=980)
    pc.save()

    pc = PC.objects.create(code=12, model=Product.objects.get(model=1233), speed=800, ram=128, hd=20, cd='50x', price=970)
    pc.save()


def insert_into_laptop():
    laptop = Laptop.objects.create(code=1, model=Product.objects.get(model=1298), speed=350, ram=32, hd=4, screen=11, price=700)
    laptop.save()

    laptop = Laptop.objects.create(code=2, model=Product.objects.get(model=1321), speed=500, ram=64, hd=8, screen=12, price=970)
    laptop.save()

    laptop = Laptop.objects.create(code=3, model=Product.objects.get(model=1750), speed=750, ram=128, hd=12, screen=14, price=1200)
    laptop.save()

    laptop = Laptop.objects.create(code=4, model=Product.objects.get(model=1298), speed=600, ram=64, hd=10, screen=15, price=1050)
    laptop.save()

    laptop = Laptop.objects.create(code=5, model=Product.objects.get(model=1752), speed=750, ram=128, hd=10, screen=14, price=1150)
    laptop.save()

    laptop = Laptop.objects.create(code=6, model=Product.objects.get(model=1298), speed=450, ram=64, hd=10, screen=12, price=950)
    laptop.save()


def insert_into_printer():
    printer = Printer.objects.create(code=1, model=Product.objects.get(model=1276), color='n', type='Laser', price=400)
    printer.save()

    printer = Printer.objects.create(code=2, model=Product.objects.get(model=1433), color='y', type='Jet', price=270)
    printer.save()

    printer = Printer.objects.create(code=3, model=Product.objects.get(model=1434), color='y', type='Jet', price=290)
    printer.save()

    printer = Printer.objects.create(code=4, model=Product.objects.get(model=1401), color='n', type='Matrix', price=150)
    printer.save()

    printer = Printer.objects.create(code=5, model=Product.objects.get(model=1408), color='n', type='Matrix', price=270)
    printer.save()

    printer = Printer.objects.create(code=6, model=Product.objects.get(model=1288), color='n', type='Laser', price=400)
    printer.save()