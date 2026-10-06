
# Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, ponlos en mayúsculas y únelos con ' | ' como separador.
colores="rojo,verde,azul,amarillo"
separar=colores.split(",")
mayuscula=colores.upper()
unir=" | ".join(separar)

print("La cadena original es :", colores)
print("La cadena separada es :", separar)
print("La cadena en mayusculas es :", mayuscula)
print("La cadena unida con ' | ' es :", unir)
