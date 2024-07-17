# Solicitar al usuario que ingrese la cantidad de macetas en una caja
cantidad_macetas = int(input("Introduce la cantidad de macetas que contiene una caja: "))

# Solicitar al usuario que ingrese el número total de cajas que necesita
total_cajas = int(input("Introduce el número total de cajas que necesitas: "))

# Solicitar al usuario que ingrese la cantidad de colores de flores que tiene
cantidad_colores = int(input("Introduce la cantidad de colores de flores que tienes: "))

# Inicializar una lista para almacenar la cantidad de macetas de cada color
macetas_por_color = []

# Pedir al usuario la cantidad de macetas para cada color
for i in range(cantidad_colores):
    cantidad = int(input(f"Introduce la cantidad de macetas para el color {i + 1}: "))
    macetas_por_color.append(cantidad_colores)

# Calcular el total de macetas para calcular porcentajes
total_macetas = sum(macetas_por_color)
print(total_macetas)

# Calcular el porcentaje de cada color
porcentajes = [cantidad_colores / total_macetas for cantidad_colores in macetas_por_color]
print(porcentajes)

# Inicializar la lista de distribución de macetas en cajas
cajas = [0] * total_cajas

# Función para encontrar la caja con el menor número de macetas para equilibrar la distribución
def encontrar_min_caja(cajas):
    return cajas.index(min(cajas))

# Distribuir las macetas en las cajas siguiendo los porcentajes
for i in range(total_macetas):
    # Encontrar el color que debe recibir una maceta basándose en porcentajes y distribución restante
    for j, porcentajes in enumerate(porcentajes):
        macetas_a_distribuir = int(total_macetas * porcentajes)
        if macetas_por_color[j] > 0 and i < macetas_a_distribuir:
            caja_min = encontrar_min_caja(cajas)
            cajas[caja_min] += 1
            macetas_por_color[j] -= 1
            print(caja_min)
            print(macetas_a_distribuir)
            print(macetas_por_color)
            break