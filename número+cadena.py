try:
    numero = int(input("Ingresá un número: "))
    cadena = input("Ingresá una cadena de texto: ")
    
    resultado = numero + cadena
    print(f"El resultado de la suma es: {resultado}")
    
except TypeError:
    print("Error: No se puede sumar un número y una cadena.")