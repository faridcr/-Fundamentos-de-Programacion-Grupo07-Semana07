# ---------- Parsear CSV manualmente ----------
lineas = [
    "Kevin,10,Ica",
    "Farid,15,Cusco",
    "Andy,13,Tacna",
]
 
print(f"{'Nombre':<10}{'Nota':>5}  Ciudad")
for linea in lineas:
    nombre, nota, ciudad = linea.split(",")
    print(f"{nombre:<10}{nota:>5}  {ciudad}")
