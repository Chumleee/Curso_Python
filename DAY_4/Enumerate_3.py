'''Práctica Enumerador 3

Imprime en pantalla únicamente los índices de aquellos nombres de la
lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina",
"Marta", "Darío", "Emiliano", "Melisa"]'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina",
"Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):

    if nombre.startswith("M"):
        print(indice)

