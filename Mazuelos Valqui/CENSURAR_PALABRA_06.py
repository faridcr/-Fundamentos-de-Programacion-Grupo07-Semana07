# ---------- Ejercicio 6: Censurar palabras ----------
texto = "¡Cállate, imbecil! Eres un cojudo y un bruto. ¡Ándate a la mierda, conchatumadre! Ven p causa, si eres hombre, imbecil."
prohibidas = ["conchatumadre", "imbecil", "cojudo", "bruto", "mierda"]

for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)