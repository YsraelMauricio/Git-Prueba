from random import randint

nombre = input("Ingrese su nombre: ")
print(f"""Bueno {nombre}, he pensado un número entre 1 y 100 
Y tienes solo ocho intentos para adivinar cuál crees que es el número""")

while True:
    numero_elegido = input(f"{nombre} digita un numero entre 1 y 100: ")
    if numero_elegido.isdecimal():
        numero_elegido = int(numero_elegido)
        break
    else:
        print("Elegiste un caracter invelido, vuelve a intentar")


numero_pensado = randint(1, 100)
numero_intentos = 8
contador_intentos = 1

while numero_intentos > 1:
    if numero_elegido not in range(1,101):
        numero_intentos -= 1
        print(f"Elejiste un numero que no esta permitido, te quedan {numero_intentos} intentos")
        numero_elegido = int(input(f"{nombre} digita un numero entre 1 y 100: "))
        contador_intentos += 1

    elif numero_elegido < numero_pensado:
        numero_intentos -= 1
        print(f"Respuesta incorrecta, elejiste un numero menor al numero secreto, te quedan {numero_intentos} intentos")
        numero_elegido = int(input(f"{nombre} digita un numero entre 1 y 100: "))
        contador_intentos += 1

    elif numero_elegido > numero_pensado:
        numero_intentos -= 1
        print(f"Respuesta incorrecta, elegiste un numero mayor al numero secreto, te quedan {numero_intentos} intentos")
        numero_elegido = int(input(f"{nombre} digita un numero entre 1 y 100: "))
        contador_intentos += 1

    elif numero_elegido == numero_pensado:
        print(f"Respuesta correcta! ganaste en tu intento {contador_intentos} felicidades")
        break
else:
    print("Lo siento, perdiste! el numero secreto era {}".format(numero_pensado))



