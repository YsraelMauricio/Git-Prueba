from random import choice

#Palabra secreta
def palabra_secreta():
    lista_secreta = ['python', 'programacion', 'mauricio']
    palabra_elegida = choice(lista_secreta)
    return palabra_elegida


#Guiones de palabra secreta
def guiones(palabra):
    guiones = []
    lista = list(palabra)
    for letra in lista:
        guiones.append("-")
    return guiones


#Eleccion de letra por turno del usuario y validacion
def turno_usuario():
    turno = input("Digita una letra: ").lower()
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while turno not in abecedario:
        print("Elige una letra valida del abecedario")
        turno = input("Digita una letra: ")
    return turno


#Comprobacion de letra en palabra, reemplazar letras por guiones
def comprobacion(letra_elegida, palabra, guiones):
    palabra_lista = list(palabra)
    letra_incorrecta = ""
    indice_letra = 0
    for letra in palabra_lista:
        if letra_elegida == letra:
            guiones.pop(indice_letra)
            guiones.insert(indice_letra,letra)
            indice_letra += 1
        else:
            indice_letra += 1
    else:
        if letra_elegida not in guiones:
            letra_incorrecta = letra_elegida
    return guiones, letra_incorrecta


#Lista de incorrectas
def lista_incorrectas(letra, lista):
    lista.append(letra)
    return lista


#Vidas
def vidas_usuario(lista):
    vidas = 8
    for letra in lista:
        vidas -=1
    return vidas


#Prograna
palabra_secreta = palabra_secreta()
guiones_palabra = guiones(palabra_secreta)
lista_letras_incorrectas = []
vidas = 1

print("Bienvenido al juego del ahorcado!")
print(f"La palabra secreta esta formada por {guiones_palabra}.")

while vidas > 0:
    letra_elegida = turno_usuario()
    letra_descubierta, letra_incorrecta = comprobacion(letra_elegida, palabra_secreta, guiones_palabra)

    if letra_elegida in palabra_secreta:
        print("Bien, tu letra esta dentro de la palabra.")
        print(letra_descubierta)
        if letra_descubierta == list(palabra_secreta):
            print(f"Felicidades ganaste!!! la palabra secreta es: '{palabra_secreta}.'")
            break
    else:
        lista_letras_incorrectas = lista_incorrectas(letra_incorrecta, lista_letras_incorrectas)
        vidas = vidas_usuario(lista_letras_incorrectas)
        print("Elegiste una letra incorrecta. Letra(s) incorrecta(s):")
        print(lista_letras_incorrectas)
        print(f"Te quedan {vidas} vidas.")
else:
    print(f"Lo siento, perdiste te quedan {vidas} vidas.\nLa palabra secreta era '{palabra_secreta}.'")