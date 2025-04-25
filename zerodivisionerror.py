try:
    numero1 = float(input("Ingresá el primer número: "))
    numero2 = float(input("Ingresá el segundo número"))
    
    resultado = numero1 / numero2
    print(f"El resultado de la división es: {resultado}")
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")