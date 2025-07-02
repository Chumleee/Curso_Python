

frase  = input("Ingrese una frase o parrafo: ").lower()#convierte la frase en minuscula

letras = (input("Ingrese 3 letras al azar separadas por espacios: ").lower()).split()# a g f

print(letras)

cantidad_letras1 = frase.count(letras[0])#cuenta la cantidas de x letra en la frase

print(f"Se ha encontrasdo la letra '{letras[0]}' repetida {cantidad_letras1} veces")

conteo = frase.split()#pasar la frase a una lista

print(f"\n {conteo}")

print(f"\nHay {len(conteo)} palabras en la frase que escribiste")#mostrar cuantas pa'labras hay en la frase

print("\nLa primer letra de tu frase es: " + frase[0] + "\nLa ultima Letra de tu frase es: " + frase[-1])

#print(frase)

inversa = " ".join(conteo[::-1]) #invierte los valores de la lista

print(f"\ntu frase inversa se vería asi: {inversa}")

print("\n")

if(("python" in frase) == True):

    print("La palabra PYTHON SI se encuentra en tu frase")
else:
    print("La palabra PYTHON NO se encuentra en tu frase")

    




    