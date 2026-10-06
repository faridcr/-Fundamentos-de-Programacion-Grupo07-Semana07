
# Dadas varias líneas CSV con formato 'nombre,nota,ciudad', extrae la información y muestra un reporte formateado.
lines = [
    "Juan,85,Madrid",
    "María,92,Barcelona",
    "Pedro,78,Valencia"
]

for line in lines:
    nombre, nota, ciudad = line.split(',')
    print(f"Nombre: {nombre}, Nota: {nota}, Ciudad: {ciudad}")