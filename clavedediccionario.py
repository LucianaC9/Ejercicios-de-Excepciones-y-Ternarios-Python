# Diccionario
datos = {
    "nombre": "Luciana",
    "edad": 23
}

while True:
    clave = input("Ingresa la clave que deseas buscar en el diccionario: ")

    try:
        valor = datos[clave]
        print(f"Valor encontrado: {valor}")
        break  # Salir del bucle si se encuentra la clave

    except KeyError:
        print(f"Error: la clave '{clave}' no existe en el diccionario.")
        opcion = input("¿Quieres agregar esta clave al diccionario? (si/no): ")

        if opcion.lower() == 'si':
            nuevo_valor = input(f"Ingresa el valor para la clave '{clave}': ")
            datos[clave] = nuevo_valor
            print(f"Clave '{clave}' agregada con el valor '{nuevo_valor}'.")
        else:
            print("No se agregó ninguna clave. Intenta con otra clave.")
