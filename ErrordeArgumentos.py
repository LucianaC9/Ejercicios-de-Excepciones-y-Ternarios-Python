def calcular_promedio(*args):
    # Verificar si hay al menos 2 números
    mensaje = (
        f"El promedio es: {sum(args) / len(args)}"
        if len(args) >= 2
        else "❌ Error: Se requieren al menos 2 números para calcular el promedio."
    )
    return mensaje

# Ingreso de números desde el teclado
entrada = input("Ingresa al menos 2 números separados por comas: ")

# Convertir la entrada en lista de números
try:
    numeros = [float(n.strip()) for n in entrada.split(",") if n.strip() != ""]
    print(calcular_promedio(*numeros))
except ValueError:
    print("❌ Error: Solo se deben ingresar números válidos.")
