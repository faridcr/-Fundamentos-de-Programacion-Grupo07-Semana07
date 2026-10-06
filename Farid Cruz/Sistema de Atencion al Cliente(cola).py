"""
EJERCICIO 3 - SISTEMA DE ATENCIÓN AL CLIENTE (Cola)

Enunciado:
Simula el sistema de turnos de un banco usando una Cola (Queue).
Los clientes esperan en orden de llegada.

a) Implementar tomar_turno(cliente) -> cliente entra a la cola.
b) Implementar atender() -> el primer cliente de la cola es atendido (sale).
c) Implementar mostrar_cola() -> mostrar cuántos esperan y sus nombres.
d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos.

Concepto:
Las colas bancarias, de impresión y de servidores son FIFO en computación.
"""

from collections import deque

cola = deque()  # la cola


def tomar_turno(cliente):
    """Agrega el cliente al final de la cola (enqueue)."""
    cola.append(cliente)
    print(f"{cliente} tomó turno.")


def atender():
    """Atiende al primer cliente de la cola (dequeue)."""
    if not cola:
        print("No hay clientes esperando.")
        return
    cliente = cola.popleft()
    print(f"Atendiendo a: {cliente}")


def mostrar_cola():
    """Muestra cuántos clientes esperan y sus nombres."""
    if not cola:
        print("La cola está vacía.")
        return
    print(f"Clientes esperando: {len(cola)}")
    print(f"Cola actual: {list(cola)}")


# ── Simulación ──────────────────────────────────────────────
# 4 clientes entran
tomar_turno("Farid")
tomar_turno("Andy")
tomar_turno("Josué")
tomar_turno("Kevin")
mostrar_cola()

# se atienden 2
atender()
atender()
mostrar_cola()

# entra 1 más
tomar_turno("Italo")
mostrar_cola()

# se atienden todos
atender()
atender()
atender()
mostrar_cola()

atender()  # prueba extra: caso límite, la cola ya está vacía