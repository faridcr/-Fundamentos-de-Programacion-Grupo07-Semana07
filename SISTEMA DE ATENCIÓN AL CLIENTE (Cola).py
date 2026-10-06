# Creamos una cola vacía para almacenar a los clientes
cola = []


# Función para agregar un cliente a la cola
def tomar_turno(cliente):
    # Agregamos el cliente al final de la cola
    cola.append(cliente)
    print(f"{cliente} entró a la cola.")


# Función para atender al primer cliente
def atender():
    # Verificamos que haya clientes esperando
    if len(cola) > 0:
        # Sacamos al primer cliente de la cola
        cliente = cola.pop(0)
        print(f"Atendiendo a: {cliente}")
    else:
        print("No hay clientes esperando.")


# Función para mostrar los clientes que están esperando
def mostrar_cola():
    print(f"\nClientes esperando: {len(cola)}")

    # Recorremos la cola para mostrar los nombres
    for cliente in cola:
        print(f"- {cliente}")


# -------------------------------
# SIMULACIÓN DEL EJERCICIO
# -------------------------------

# Entran 4 clientes
tomar_turno("Juan")
tomar_turno("Pedro")
tomar_turno("María")
tomar_turno("Carlos")

# Mostramos la cola
mostrar_cola()

# Se atienden 2 clientes
atender()
atender()

# Entra un cliente más
tomar_turno("Luis")

# Mostramos nuevamente la cola
mostrar_cola()

# Se atienden todos los clientes restantes
atender()
atender()
atender()

# Mostramos la cola final
mostrar_cola()