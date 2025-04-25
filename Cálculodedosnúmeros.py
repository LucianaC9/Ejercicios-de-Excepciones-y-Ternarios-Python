# Ingresar dos números desde el teclado
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Usar operador ternario para encontrar el mayor
mayor = a if a > b else b

# Mostrar el resultado
print(f"El número mayor es: {mayor}")
