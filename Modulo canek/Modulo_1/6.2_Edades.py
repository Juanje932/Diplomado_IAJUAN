def categorizar_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"

# Pedir la edad al usuario
try:
    edad = int(input("Ingresa tu edad: "))
    categoria = categorizar_edad(edad)
    print(f"Perteneces a la categoría: {categoria}")
except ValueError:
    print("Por favor, ingresa un número válido.")
    