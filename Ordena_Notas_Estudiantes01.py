#Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
[85, 42, 93, 67, 28, 75]

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
 
def selection_sort(l):
    for i in range(len(l) - 1):
        m = i
        for j in range(i + 1, len(l)):
            if l[j] < l[m]:
                m = j
        l[i], l[m] = l[m], l[i]
 
notas = [85, 42, 93, 67, 28, 75]
 
a = notas.copy(); bubble_sort(a)
b = notas.copy(); selection_sort(b)
 
print("Bubble Sort:   ", a)
print("Selection Sort:", b)
print("Mín:", a[0], "| Máx:", a[-1], "| Promedio:", sum(a) / len(a))