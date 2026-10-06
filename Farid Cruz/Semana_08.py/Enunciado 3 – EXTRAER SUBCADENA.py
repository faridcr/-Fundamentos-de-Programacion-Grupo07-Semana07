# Ejercicio 3 - Extraer subcadena
# Enunciado: Dada la cadena 'Análisis de Datos con Python',
# extraer las palabras 'Datos' y 'Python' usando slicing.

# 1. Definir la cadena original
texto = "Análisis de Datos con Python"

# 2. Extraer 'Datos' con slicing: empieza en el índice 12 y termina antes del 17
palabra1 = texto[12:17] #Datos

# 3. Extraer 'Python' con slicing: empieza en el índice 22 hasta el final
palabra2 = texto[22:] #Python

# 4. Mostrar los resultados
print(f"Palabra 1: {palabra1}") #Datos
print(f"Palabra 2: {palabra2}") #Python