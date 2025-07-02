
#explicacion de diccionarios

cliente = {'Nombre':'Raul','Apellido':'Gonzalez','Edad':24}

consulta = (cliente['Edad'])

print(f"edad cliente {consulta}")#imprime la consulta de la llave edad

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'c2':200}}

print(dic['c2'][1])#imprime la consulta de la llave c2 pero en el indice indicado de la lista


dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}

print(dic2['c2'][1].upper())#imprime lo consultado en mayusculas

dic3 = {1:'a',2:'b'}

print(dic3)

dic3[3] = 'c' #agregar elemento al diccionario 

print(dic3)