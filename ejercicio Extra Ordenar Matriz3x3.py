def bubble_sort(lista):
    """Ordena una lista en su lugar usando Bubble Sort."""
    n = len(lista)

    for i in range(n):
        intercambiado = False

        # Comparamos elementos consecutivos
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:

                # Intercambiamos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True

        # Si no hubo cambios, ya está ordenada
        if not intercambiado:
            break


def ordenar_matriz(matriz):
    """Ordena una matriz de menor a mayor, fila por fila."""
    filas = len(matriz)
    columnas = len(matriz[0])

    # Convertimos la matriz en una sola lista
    plano = []
    for fila in matriz:
        for valor in fila:
            plano.append(valor)

    # Ordenamos todos los valores
    bubble_sort(plano)

    # Volvemos a formar la matriz
    resultado = []
    for i in range(filas):
        inicio = i * columnas
        resultado.append(plano[inicio:inicio + columnas])

    return resultado


# Prueba
matriz = [[1, 3, 4],
          [5, 8, 9],
          [2, 6, 7]]

print("Matriz original:")
for fila in matriz:
    print(fila)

ordenada = ordenar_matriz(matriz)

print("\nMatriz ordenada:")
for fila in ordenada:
    print(fila)

print()