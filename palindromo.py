
#------------- Michael Morron -------------------

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para comprar bien.
    palabra = palabra.replace(" ", "")  # Eliminamos los espacios en blanco si los hay
    return palabra == palabra[::-1]  # Comprobamos si la palabra es igual a su reverso

# Pedimos una palabra
entrada = input("Ingrese una palabra: ")

# Verificamos si es un palíndromo
if es_palindromo(entrada):
  print("|")
  print("|", "'", entrada,"'" ," Si es un palíndromo.")
  print("|")
else:
    print("|")
    print("|", "'", entrada,"'" ," No es un palíndromo.")
    print("| Palíndromo: Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.")
    print("| Ejemplo: Somos")
    print("|")
