

lista = ['a','b','c']

for i in lista:
    n_letra = lista.index(i) + 1
    print(f"Letra {n_letra}: {i}")

lista_2 = ['pablo','laura','fede','luis','julia']

for nombre in lista_2:
    if nombre.startswith('l'):#verifica si inician con l
        print(nombre)


numeros = [1,2,3,4,5]

valor = 0

for i in numeros:
    valor += i
print(valor)

palabra = 'pyhton'

for i in palabra:
    print(i)


dic = {'clave1':'a','clave2':'b','clave3':'c'}

for i in dic.items():
    print(i)