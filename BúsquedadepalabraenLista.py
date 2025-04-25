# Función que busca una palabra en una lista usando *args y operador ternario
def buscar_palabra(palabra_buscada, *args):
    resultado = "Sí está en la lista" if palabra_buscada in args else "No está en la lista"
    return resultado

# Ingreso de la lista de palabras desde el teclado
entrada = input("Ingresa una lista de palabras separadas por comas: ") #ejemplo: Computadoras,celulares,tablets
lista_palabras = [palabra.strip() for palabra in entrada.split(",")]

# Ingresa la palabra que desea buscar
palabra = input("Ingresa la palabra que deseas buscar: ") # El usuario deberá buscar una de las palabras que ingresó a la lista

# Llamada a la función
print(buscar_palabra(palabra, *lista_palabras))
