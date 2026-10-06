fruta = ["uva", "pera", "uva", "naranja"]

try:
    # Buscamos la primera aparición de "uva"
    primera = fruta.index("uva")

    # Buscamos la segunda "uva", comenzando después de la primera
    segunda = fruta.index("uva", primera + 1)

    # Eliminamos la segunda "uva" encontrada
    fruta.pop(segunda)

except ValueError:
    # Se ejecuta si no existe una segunda "uva"
    print("No hay una segunda uva.")

# Mostramos la lista después de eliminar
print(fruta)