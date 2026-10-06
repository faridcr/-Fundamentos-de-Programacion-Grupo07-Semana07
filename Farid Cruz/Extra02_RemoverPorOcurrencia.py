""""
fruta = ["uva", "pera", "uva", "naranja", "uva", "kiwi", "uva"]

try:
    primera = fruta.index("uva")
    segunda = fruta.index("uva", primera + 1)
    tercera = fruta.index("uva", segunda + 1)
    fruta.pop(tercera)
except ValueError:
    print("No hay una tercera uva.")    

print(fruta)  # fruta = ['uva', 'pera', 'uva', 'naranja', 'kiwi', 'uva']
"""
def eliminar_ocurrencia(lista, elemento, n=1):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1
            if contador == n:
                lista.pop(i)
                return True
    return False


fruta = ["uva", "pera", "uva", "naranja", "uva", "kiwi", "uva"]
print(f"Lista actual: {fruta}")

n = int(input("¿Qué uva quieres eliminar? (1, 2, 3...): "))

if eliminar_ocurrencia(fruta, "uva", n):
    print(f"Se eliminó la uva número {n}.")
else:
    print(f"No hay una uva número {n}.")

print(fruta)