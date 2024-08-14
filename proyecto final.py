#factura de compra

def main():

    from menu import item
    from menu import menu

    def additem(name, price):
        menufile = open('menu.py', 'a')
        menufile.write(f'\nmenu.append( item( {name}, {price} ) )')
        menufile.close()
        menu.append(item(name, price))
        
    def finditem(a):
        for product in menu:
            if product.name == a:
                return product

    impuesto = 8.875; impuesto /= 100

    def openmenu():
        result = '*'*90 + '\n'
        for item in menu:
            result += item.name + f' | precio: {item.price}' + f' | cantidad disponible: {item.cantidaddisponible}' + '\n'

        result += '*'*90
        print( result )
    
    def cleaninput(string):
        return input(string).strip().lower()

    def total():
        a = 0
        for product in menu:
            a += product.price*product.cantidadcarrito
        return a
    
    def vercarrito():
        factura = '*'*90 + '\n'
        for product in menu:
            if product.cantidadcarrito > 0:
                factura += product.name + '|cantidad: ' + str(product.cantidadcarrito) + '\n'
        factura += f'subtotal = {total()}\n'
        factura += f'total (con impuesto) = {int( total()*(1+impuesto) )}\n'
        factura += '*'*90
        if total() == 0:
            return print('no tiene nada en el carrito')
        print(factura)

    print('bienvenido a la tienda')

    while True:
        index = None
        while not index:
            item = cleaninput('que desea comprar? (\'vm\' para ver menu) (\'salir\' para salir) (\'vc\' para ver carrito)')
            if item == 'salir':
                return
            index = finditem(item)
            if not index:
                if item == 'vm':
                    openmenu()
                    continue

                if item == 'vc':
                    vercarrito()
                    continue

                print('invalid item')

        cantidad = int( cleaninput('que cantidad desea comprar? (ingrese cantidades negativas para quitar items del carrito)') )
        while index.cantidadcarrito + cantidad < 0:
            print('no puede tener cantidades negativas en el carrito')
            cantidad = int( cleaninput('que cantidad desea comprar/quitar?') )

        index.cantidadcarrito += cantidad
        
        while index.cantidadcarrito > index.cantidaddisponible:
            print('lamento decirte que no tenemos la cantidad que solicita')
            index.cantidadcarrito -= cantidad

            cantidad = int( cleaninput('que cantidad desea comprar/quitar?') )
            index.cantidadcarrito += cantidad

        if cleaninput('desea comprar algo mas? (y/n)') == 'n':
            print('\nmuchas gracias por su compra')
            break

    vercarrito()

main()