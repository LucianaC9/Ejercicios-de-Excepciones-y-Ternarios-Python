# Función para calcular el promedio usando *args y operador ternario
def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio

# Ejemplo de uso: El usuario ingresa números: 1, 2, 3
print("Ingresa los números separados por comas:")
entrada = input()
# Convertir la entrada a una lista de números
numeros = [float(n.strip()) for n in entrada.split(",")]

# Llamar a la función con *args
resultado = calcular_promedio(*numeros)
print(f"El promedio es: {resultado}")
