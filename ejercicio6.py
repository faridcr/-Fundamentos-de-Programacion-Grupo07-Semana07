
# Dada una lista de palabras prohibidas, reemplaza cada aparición en un texto por asteriscos del mismo largo.
pala_prohibidas=["feo","tonto","idiota","mongol"]
texto="El es tonto , feo , idiota , mongol , pero asi es mi amigo"
print("El texto original es :", texto)
for palabra in pala_prohibidas:
    texto=texto.replace(palabra,"*" * len(palabra))

print("El texto modificado es :", texto)