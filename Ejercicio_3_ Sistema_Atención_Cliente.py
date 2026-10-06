cola = []

def tomar_turno(cliente):
    cola.append(cliente)
    print("Entró:", cliente)
    print("Cola:", cola)
    print()


def atender():
    if len(cola) > 0:
        cliente = cola.pop(0)
        print("Atendiendo a:", cliente)
    else:
        print("No hay clientes en la cola")
    print()


def mostrar_cola():
    print("Clientes esperando:", len(cola))
    print("Cola:", cola)
    print()


# Entran 4 clientes
tomar_turno("Carlos")
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("María")

# Mostrar cola
mostrar_cola()

# Se atienden 2
atender()
atender()

# Entra 1 más
tomar_turno("Pedro")

# Mostrar cola
mostrar_cola()

# Se atienden todos
while len(cola) > 0:
    atender()

# Mostrar cola final
mostrar_cola()