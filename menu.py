import math
class item:
    def __init__(self, name, price, cantidaddisponible = math.inf, cantidadcarrito = 0):
        self.name = name
        self.price = price
        self.cantidadcarrito = cantidadcarrito
        self.cantidaddisponible = cantidaddisponible

menu = [
    item('agua', 20, 10), 
    item('laptop', 50000),
    item('pan', 15),
    item('manzana', 50),
    item('celular', 20000)
    ]