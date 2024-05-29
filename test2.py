lista = []
vocales = ['a', 'e', 'i', 'o', 'u']

for i in range(2):
    print(i)
    lista.append(input('Ingrese el siguiente nombre: ')) ### no se puede usar lista[i] =, ya que no se ha creado ningun elemento tdoavia

for nombre in lista:

    numvoc = 0
    for letra in nombre:

        if letra in vocales:
            numvoc += 1

    if numvoc >= 3:
        print(nombre + ' este nombre tiene 3 vocales o mas')
