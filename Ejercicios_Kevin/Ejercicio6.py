

# Enunciado 6 - CENSURAR PALABRA EN UN TEXTO

texto = "Python es malo y aburrido"

prohibidas = ["malo", "aburrido"]

for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)

print("\n------CENSURAR LETRAS EN UNA PALABRA------\n")
palabra = "Python"

resultado = "**" + palabra[2:]

print(resultado)