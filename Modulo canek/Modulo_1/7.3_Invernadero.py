
def analizar_punto(temperatura, humedad):
    temperatura = 30
    humedad = 30
    if temperatura > 30:
        if humedad < 30:
            return "Recomendación: Riego y ventilación"
        else:
            return "Recomendación: Ventilación"
    else:
        if humedad < 30:
            return "Recomendación: Riego"
        else:
            return "Recomendación: No se necesitan acciones"
def realizar_analisis(numero_de_puntos):
    for i in range(numero_de_puntos):
        temperatura, humedad = obtener_datos_temperatura_y_humedad()
        print(f"Análisis del punto {i + 1}")
        recomendacion = analizar_punto(temperatura, humedad)
        print(recomendacion)

# Ejemplo de uso:
numero_de_puntos = 3
realizar_analisis(numero_de_puntos)