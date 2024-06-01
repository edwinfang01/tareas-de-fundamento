def operacion(op, a,b):
    if op == 0:
        return a+b
    elif op == 2:
        return a*b
    elif op == 1:
        return a-b
    elif op == 3:
        return a/b


salir = False

while not salir:

    texto = input('hola que operacion quiere hacer? (0/suma) (1/resta) (2/multiplicacion) (3/division)')
    numeros = []
    numeros.append( input('ingrese el primer numero') )
    numeros.append( input('ingrese el segundo numero') )

    print(operacion(int(texto), int(numeros[0]), int(numeros[1])))
    if input('desea continuar (0/salir) (1/continuar)') == '0':
        salir = True # o puede usar break en vez
