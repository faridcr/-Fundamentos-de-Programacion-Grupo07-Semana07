# ---------- Dividir y unir palabras ----------

colores = "rojo,verde,azul,amarillo"
lista = colores.split(",")
mayusculas = [c.upper() for c in lista]
print(" | ".join(mayusculas))