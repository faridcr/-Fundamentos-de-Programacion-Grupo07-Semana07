
# Dada la cadena ' Python es divertido ', elimina los espacios en los extremos y cuenta cuántos caracteres tiene la
# cadena limpia

frase=" Python es divertido "
limpio=frase.strip()
limpio_inicio=frase.lstrip()
limpio_final=frase.rstrip()
sin_espacios=frase.replace(" ","")
print("La cadena limpia es      :",limpio)
print("Sin espacion al inicio es:",limpio_inicio)
print("sin espacio al final es  :",limpio_final)
print("sin espacios en blanco   :",sin_espacios)
print("tiene ", len(limpio), "caracteres")