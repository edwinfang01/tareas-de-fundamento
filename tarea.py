nombres = ['juan', 'jesus', 'maria', 'mario']
nombres_con_j = [] #operacion filtrar
for nombre in nombres:
    if 'j' in nombre:
        nombres_con_j.append(nombre)

tupla = (0,1,2,3) #operacion con tupla
valor = 0
for i in tupla:
    valor += tupla[i]
print(valor)

diccionario = {'hola': 'mi nombre es', 'joerlyn': 'profe'} #modificando un diccionario
diccionario['joerlyn'] = None
print(diccionario['joerlyn'])