def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

# Solicita al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Determina si el número es par o impar y muestra el resultado
resultado = es_par_o_impar(numero)
print(resultado)