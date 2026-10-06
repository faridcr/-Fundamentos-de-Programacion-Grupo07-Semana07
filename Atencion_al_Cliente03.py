#Simula el sistema de turnos de un banco usando una Cola (Queue). Los clientes esperan en orden de llegada.

from collections import deque

cola = deque()

def tomar_turno(cliente):
    cola.append(cliente)
    print("Entra:", cliente)

def atender():
    if cola:
        print("Atendido:", cola.popleft())
    else:
        print("No hay clientes en espera")

def mostrar_cola():
    print(f"En espera ({len(cola)}):", list(cola))

# d) Simulación
for c in ["Ana", "Luis", "María", "Pedro"]:
    tomar_turno(c)
mostrar_cola()

atender()
atender()
mostrar_cola()

tomar_turno("Sofía")
mostrar_cola()

while cola:
    atender()
mostrar_cola()