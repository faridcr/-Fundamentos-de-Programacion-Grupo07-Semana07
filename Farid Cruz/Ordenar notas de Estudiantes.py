def bubble_sort(lista):
    """Ordena una lista en su lugar usando Bubble Sort."""
    n = len(lista)                      # n = total de elementos
    for i in range(n):                  # i = pasada actual (0 a n-1)
        intercambiado = False           # optimización: detectar lista ya ordenada
        for j in range(0, n - i - 1):   # j recorre hasta el último no colocado
            if lista[j] > lista[j + 1]: # ¿elemento actual mayor que el siguiente?
                # Si sí, se intercambian (swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True    # hubo al menos 1 cambio
        if not intercambiado:           # si no hubo cambios → lista ordenada
            break                       # ¡salir antes! (optimización)




def selection_sort(lista):
    """Ordena una lista en su lugar usando Selection Sort."""
    n = len(lista)                          # cantidad de elementos
    for i in range(n - 1):                  # i = inicio sublista sin ordenar
        # Asumir que el mínimo es el primero de la sublista
        idx_min = i                         # guarda índice del mínimo actual
        for j in range(i + 1, n):           # buscar mínimo en el resto
            if lista[j] < lista[idx_min]:   # ¿encontré algo menor?
                idx_min = j                 # actualizo el índice del mínimo
        # Solo intercambiar si el mínimo no era ya el primero
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]  # swap


# ── Ejemplo de uso ──────────────────────────────────────────
notas = [85, 42, 93, 67, 28, 75]

# a) Bubble Sort (sobre una copia)
notas_bubble = notas.copy()
bubble_sort(notas_bubble)
print(f"Bubble Sort:   {notas_bubble}")

# b) Selection Sort (sobre otra copia)
notas_selection = notas.copy()
selection_sort(notas_selection)
print(f"Selection Sort: {notas_selection}")

# Comparar resultados
print(f"¿Mismo resultado? {notas_bubble == notas_selection}")

# c) Mínima, máxima y promedio
print(f"Nota mínima: {notas_bubble[0]}")
print(f"Nota máxima: {notas_bubble[-1]}")
print(f"Promedio:   {sum(notas_bubble) / len(notas_bubble)}")