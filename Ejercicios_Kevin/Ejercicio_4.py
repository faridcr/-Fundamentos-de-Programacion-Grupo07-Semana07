#Enunciado4 –DIVIDIR Y UNIR PALABRAS:


colorcitos = "rojo,verde,azul,amarillo".upper().split(",")

resultado = " | ".join(colorcitos)

print(f"Colores: {resultado}")