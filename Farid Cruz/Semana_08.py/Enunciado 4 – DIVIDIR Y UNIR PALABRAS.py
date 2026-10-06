# Ejercicio 4 - Dividir y unir palabras
# Enunciado: Dada la cadena 'rojo,verde,azul,amarillo', separar los colores,
# ponerlos en mayúsculas y unirlos con ' | ' como separador.

# 1. Definir la cadena original
cadena = "rojo,verde,azul,amarillo"

# 2. Separar los colores por la coma con split(), que devuelve una lista
colores = cadena.split(",")

# 3. Poner cada color en MAYÚSCULAS con upper()
colores_mayusculas = []
for color in colores:
    colores_mayusculas.append(color.upper())

# 4. Unir los colores con ' | ' usando join()
resultado = " 1 ".join(colores_mayusculas)

# 5. Mostrar el resultado
print(resultado)