#Inicializar el contador

contador = 0

while contador <3:
    temperatura = float(input('ingrese la temperatura:  '))

    humedad = float(input(Ingrese la humedad:  ))

    if temperatura > 30:
        if humedad >= 30:
            accion = "Se recomienda ventilacion"
        else:
            accion = "Se recomienda riego y ventilacion:
    else:
