# Ejercicio 7 - Parsear datos CSV manualmente
# Enunciado: Dadas varias líneas CSV con formato 'nombre,nota,ciudad',
# extraer la información y mostrar un reporte formateado.

# 1. Definir las líneas CSV (una por renglón)
csv = """Farid,17,Lima
Kevin,15,Ica
Josue,16,Arequipa
Andy,17,Cusco
Italo,17,Piura"""

# 2. Encabezado del reporte
print("REPORTE DE ESTUDIANTES")
print("-" * 45)

# 3. Separar el texto en líneas con splitlines() y recorrer cada una
for linea in csv.splitlines():
    # 4. Separar cada línea por la coma con split(",") y guardar en 3 variables
    nombre, nota, ciudad = linea.strip().split(",")

    # 5. Mostrar los datos formateados (la nota se convierte a número con 2 decimales)
    print(f"Estudiante: {nombre} | Nota: {float(nota):.2f} | Ciudad: {ciudad}")