nombre_archivo = input("Ingresa el nombre del archivo que deseas abrir: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")

    crear = input(f"¿Deseas crear el archivo '{nombre_archivo}'? (si/no): ").strip().lower()

    if crear == 'si':
        try:
            with open(nombre_archivo, 'w') as nuevo_archivo:
                print(f"Se ha creado un nuevo archivo llamado '{nombre_archivo}'.")
        except Exception as e:
            print(f"No se pudo crear el archivo. Error: {e}")
    else:
        print("No se creó ningún archivo.")
