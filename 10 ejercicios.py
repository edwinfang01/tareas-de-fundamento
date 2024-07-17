import math

def ejercicios(a = None, uso = 'usar', *, ejercicio = 1): # escribir mostrar para mostrar la lista
    lista = []

    for i in range(10):
        lista.append( int ( input('ingrese un numero entero') ) )

    def isprime(n):
        count = 0
        for i in range(2, n):
            if n % i  == 0:
                count += 1
                break
        return count == 0
    
    match ejercicio:
        case 1:
            lista = lista.index( max(lista) )

        case 2:
            lista = lista.index( max( [num for num in lista if num%2 == 0] ) )
        
        case 3:
            lista = lista.index( max( [num for num in lista if isprime(num)] ) )

        case 4:
            lista = len ( [num for num in lista if isprime( float( str(num)[0] ) )] )
        
        case 5:
            lista = [num for num in lista if isprime(num)]

            numero_con_mayor = {'valor': None, 'digitospares': 0}
            for numero in lista:
                digitospares = 0

                for b in str(numero):
                    if float(b) % 2 == 0:
                        digitospares += 1

                if numero_con_mayor['digitospares'] < digitospares:
                    numero_con_mayor['valor'], numero_con_mayor['digitospares'] = numero, digitospares

            print(lista)
            lista = lista.index( numero_con_mayor['valor'] )
        
        case 6:
            empiezan = [num for num in lista if len( str(num) ) > 3]
            lista = [lista.index(num) for num in empiezan]
        
        case 7:
            lista = sum(lista) / len(lista)

        case 8:
            lista = len( [num for num in lista if num < 0] )

        case 9:
            lista = [math.factorial(num) for num in lista]

        case 10:
            lista = len ( list( set( [num for num in lista if a % num == 0] ) ) )

    if uso == 'mostrar':
        print(lista)
    return lista

ejercicios(50, ejercicio=5, uso = 'mostrar')

#en el ejercicio 5 toma los ceros como digitos pares, ya que cero entre 2 es cero, es un entero