def getdigits(a, b):
    num = str(a)
    return int(num[b-1:b])

def showdigits(a):
    txt = ''
    a = str(a)
    for i in range(1, len(a)+1):
        if i > 1:
            txt += ', '
        txt += str(getdigits(a, i))
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
    if getdigits(dif, len(str(dif))) == 4:
        showdigits(dif)
    if dif < 10 and primo(dif):
        print(a*b)

ejercicio12(26, 0)