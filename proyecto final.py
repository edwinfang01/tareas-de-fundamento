#factura de compra

def main():

    menu = {'item1': 30, 'item2': 50, 'item3': 20}

    carrito = menu.copy()
    for item in carrito:
        carrito[item] = 0

    total = 0

    while True:
        item = input('que quiere comprar?').strip().lower() 
        cantidad = int( input('que cantidad desea comprar?') )
        carrito[item] += cantidad
        if input('desea continuar? (y/n)').lower().strip() == 'n':
            break

    factura = ''
    for item, cantidad in carrito.items():
        total += menu[item]*cantidad
        
    for item, cantidad in carrito.items():
        if cantidad > 0:
            factura += item + ' |cantidad: ' + str(cantidad) + '\n'
    factura += f'total = {total}'

    print(factura)

main() #yo lo pudiera agregar quizas una opcion para ver el menu, y quizas te calcule el impuesto