

nombres =['Ana','Hugo','Valeria']
edades = [61,25,42]
ciudades = ['Mexico','Peru','España']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edades,ciudad in combinados:

    print(f"{nombre} : {edades} : {ciudad}")