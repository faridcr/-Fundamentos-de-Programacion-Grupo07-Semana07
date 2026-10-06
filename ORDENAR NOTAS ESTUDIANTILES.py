# EJERCICIO 1 - ORDENAR NOTAS ESTUDIANTILES

# Lista de notas de los 6 estudiantes
notas = [85, 42, 93, 67, 28, 75]


# --------------------------------------------------
# a) ORDENAMIENTO BUBBLE SORT
# --------------------------------------------------

# Hacemos una copia para no modificar la lista original
bubble = notas.copy()

# Recorremos la lista varias veces
for i in range(len(bubble)):

    # Comparamos cada elemento con el siguiente
    for j in range(len(bubble) - 1 - i):

        # Si el elemento actual es mayor que el siguiente,
        # los intercambiamos
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]


# Mostramos el resultado de Bubble Sort
print("Orden con Bubble Sort:", bubble)


# --------------------------------------------------
# b) ORDENAMIENTO SELECTION SORT
# --------------------------------------------------

# Hacemos otra copia de la lista original
selection = notas.copy()

# Recorremos cada posición de la lista
for i in range(len(selection)):

    # Suponemos que la posición actual tiene
    # el número más pequeño
    minimo = i

    # Buscamos un número menor en el resto de la lista
    for j in range(i + 1, len(selection)):

        if selection[j] < selection[minimo]:
            minimo = j

    # Intercambiamos el número actual con el menor encontrado
    selection[i], selection[minimo] = selection[minimo], selection[i]


# Mostramos el resultado de Selection Sort
print("Orden con Selection Sort:", selection)


# --------------------------------------------------
# c) NOTA MÍNIMA, MÁXIMA Y PROMEDIO
# --------------------------------------------------

# La primera posición de la lista ordenada es la mínima
minima = selection[0]

# La última posición es la máxima
maxima = selection[-1]

# Calculamos el promedio sumando las notas
# y dividiendo entre la cantidad de estudiantes
promedio = sum(notas) / len(notas)


# Mostramos los resultados
print("Nota mínima:", minima)
print("Nota máxima:", maxima)
print("Promedio:", promedio)