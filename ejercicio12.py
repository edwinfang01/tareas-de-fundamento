def getdigits(a, b): #no hay que usar funcion getdigits en python
    num = str(a)
    return int(num[b-1:b])

def showdigits(a):
    txt = ''
    a = str(a)
    for i in range(len(a)):
        if i > 0:
            txt += ', '
        txt += a[i] #no hay que usar funcion getdigits en python
    print(txt)

def primo(a):
    count = 0
    for i in range(a):
        if a % (i+1) == 0:
            count += 1
    return count <= 2

def ejercicio12(a,b):
    dif = abs(a-b)
    if dif % 2 == 0:
        suma = 0
        for i in ( str(a) + str(b) ):
            suma += int(i)
        print(suma)
    if str(dif)[-1] == 4: # o getdigits(dif, len(str(dif))) == 4
        showdigits(dif)
    if dif < 10 and primo(dif):
        print(a*b)

ejercicio12(26, 0)