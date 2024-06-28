import math

def ejercicios(a = None, b = None, uso = 'usar', *, ejercicio = 1): # escribir mostrar para mostrar la lista
    lista = []
    
    match ejercicio:
        case 1:

            if b:
                return [i for i in range(a+1, b)]
            
            for i in range(1, a):
                lista.append(i)

        case 2:
            lista = [i for i in ejercicios(1, a) if i % 2 == 0]
        
        case 3:
            for i in ejercicios(a):
                if a % i == 0:
                    lista.append(i)

        case 4:
            lista = ejercicios(a, b=b) # ya se comprobo que no hay error
        
        case 5:
            lista = [i for i in ejercicios(a, b = b) if str(i)[-1] == '4']
        
        case 6:
            if len(str(a)) == 3:
                for i in str(a):
                    print( list (range(0, int (i) )) )
            return
        
        case 7:
            lista = list( range(1+1, 100) )

        case 8:
            lista = [ pares for pares in list( range(20+1, 200) ) if pares % 2 == 0 ]

        case 9:
            lista = [i for i in ejercicios(20, 205) if str(i)[-1] == '6']

        case 10:
            lista = 0
            for i in ejercicios(a):
                lista += i
        
        case 11:
            a = str(a)
            greater, smaller = int(a[0]), int(a[1])

            if greater == smaller:
                return print('se puso 2 digitos iguales')
            elif greater < smaller:
                smaller, greater = greater, smaller

            if len(a) == 2:
                lista = ejercicios( smaller, b = greater )

        case 12:
            if len( str(a) ) == 3:
                lista = '1' in str(a)
        
        case 13:
            lista = [i for i in ejercicios(a) if i % 5 == 0]

        case 14:
            lista = [i*3 for i in range(1, 20)]
        
        case 15:
            lista = 0
            for i in ejercicios(ejercicio=14):
                lista += i
        
        case 16:
            uso = 'usar'
            x, y = ejercicios(a*2, ejercicio=2), ejercicios(b*5, ejercicio=13) #a es los primeros multiplos de 2, y b son los primeros multiplos de 5
            x, y = sum(x)/len(x), sum(y)/len(y)
            print(x, y)
            if x > y:
                print(f'el promedio de los {a} primeros multiplos de 2 es mayor que el de los {b} primeros multiplos de 5')
            elif x == y:
                print(f'el promedio de los {a} primeros multiplos de 2 es igual que el de los {b} primeros multiplos de 5')
            else:
                print(f'el promedio de los {a} primeros multiplos de 2 es menor que el de los {b} primeros multiplos de 5')

        case 18:
            lista = ejercicios(10)

        case 19:
            for i in range(1, 9 + 1):
                print(f'{i} por {a} es igual a {i*a}')
            return

        case 20:
            lista = list(range(2, a)) #el limite superior no es incluido, pero el inferior si
            lista = sum([math.factorial(i) for i in lista])

    if uso == 'mostrar':
        print(lista)
    return lista

ejercicios(159, None , ejercicio=10, uso='mostrar')