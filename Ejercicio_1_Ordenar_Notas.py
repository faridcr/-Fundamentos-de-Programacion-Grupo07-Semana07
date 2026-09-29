# Lista original de notas
notas = [85, 42, 93, 67, 28, 75]


# -------------------------
# A) BUBBLE SORT
# -------------------------

notas_bubble = notas.copy()

for i in range(len(notas_bubble)):
    for j in range(len(notas_bubble) - 1):
        if notas_bubble[j] > notas_bubble[j + 1]:
            notas_bubble[j], notas_bubble[j + 1] = notas_bubble[j + 1], notas_bubble[j]

print("Bubble Sort:", notas_bubble)


# -------------------------
# B) SELECTION SORT
# -------------------------

notas_selection = notas.copy()

for i in range(len(notas_selection)):
    posicion_menor = i

    for j in range(i + 1, len(notas_selection)):
        if notas_selection[j] < notas_selection[posicion_menor]:
            posicion_menor = j

    notas_selection[i], notas_selection[posicion_menor] = notas_selection[posicion_menor], notas_selection[i]

print("Selection Sort:", notas_selection)


# -------------------------
# C) MÍNIMA, MÁXIMA Y PROMEDIO
# -------------------------

nota_minima = min(notas)
nota_maxima = max(notas)
promedio = sum(notas) / len(notas)

print("Nota mínima:", nota_minima)
print("Nota máxima:", nota_maxima)
print("Promedio:", promedio)