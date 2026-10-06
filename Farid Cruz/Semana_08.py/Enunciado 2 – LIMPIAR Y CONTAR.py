# Ejercicio 2 - Limpiar y contar
# Enunciado: Dada la cadena '   Python es divertido   ', eliminar los
# espacios en los extremos y contar cuántos caracteres tiene la cadena limpia.

# 1. Definir la cadena original (con espacios al inicio y al final)
cadena = "   Python es divertido   "

# 2. Eliminar los espacios de los extremos con strip()
cadena_limpia = cadena.strip()

# 3. Contar los caracteres de la cadena limpia con len()
cantidad = len(cadena_limpia)

# 4. Mostrar los resultados
print(f"Cadena original: '{cadena}'")
print(f"Cadena limpia: '{cadena_limpia}'")
print(f"Cantidad de caracteres: {cantidad}")