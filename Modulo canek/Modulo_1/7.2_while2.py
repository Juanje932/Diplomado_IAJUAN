numero_secreto = 3
adivinado = False
print("¡Bienvenido al juego!")
print("Adivina el número secreto entre 1 y 10")
while not adivinado:
    # Leer el número ingresado por el usuario
    intento = int(input("Introduce tu número: "))
    # Comparar el número ingresado con el número secreto
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True
    else:
        print("Intenta de nuevo")