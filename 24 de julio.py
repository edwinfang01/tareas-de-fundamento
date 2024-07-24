def saludar():
    nombre = input('cual es su nombre?')
    print(f'saludos {nombre}')

def sumar():
    num1 = float( input('escriba un numero') )
    num2 = float( input('escriba otro numero') )
    print(num1+num2)

def arearectan():
    base = float ( input('cual es la longitud de la base del rectangulo?') )
    altura = float ( input('cual es la altura del rectangulo') )
    print(base*altura)

def parimpar(n):
    par = None
    if type(n) == 'float' or type(n) == 'int':
        return n % 2 == 0

def conversiontemp(a):
    return a*1.8 + 32

def maxmimo(n): #n es un interable
    return max(n)

def palindromo(a):
    normal = list(a)
    reves = list(a); reves.reverse()
    return normal == reves

def factorial(n):
    result = 1
    for i in range(1, n):
        result = result*i

def contarvocales(a):
    a = list(a)
    vocales = ['a', 'e', 'i', 'o', 'u']
    num = 0
    for i in vocales:
        num += a.count(i)

    return num

def primo(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    
    return prime