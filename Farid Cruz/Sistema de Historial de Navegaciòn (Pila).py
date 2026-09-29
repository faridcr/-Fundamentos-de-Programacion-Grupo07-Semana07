"""
EJERCICIO 2 - SISTEMA DE HISTORIAL DE NAVEGACIÓN (Pila)

Enunciado:
Simula el historial de un navegador web usando una Pila (Stack).
El usuario visita páginas y puede retroceder.

a) Implementar visitar(url) -> agrega la página a la pila y muestra la pila actual.
b) Implementar retroceder() -> quita la última página y muestra a dónde regresó.
c) Implementar pagina_actual() -> muestra la página actual sin quitarla.
d) Probar con: Google -> YouTube -> GitHub -> retroceder -> retroceder.

Concepto:
El botón "Atrás" del navegador es un Stack en acción: LIFO.
"""

historial = []  # la pila


def visitar(url):
    """Agrega la página a la pila (push) y muestra la pila actual."""
    historial.append(url)
    print(f"Visitando: {url}")
    print(f"Pila actual: {historial}")


def retroceder():
    """Quita la última página (pop) y muestra a dónde regresó."""
    if len(historial) <= 1:
        print("No hay páginas anteriores a las que retroceder.")
        return
    historial.pop()
    print(f"Regresaste a: {historial[-1]}")
    print(f"Pila actual: {historial}")


def pagina_actual():
    """Muestra la página actual sin quitarla de la pila."""
    if not historial:
        print("No has visitado ninguna página.")
        return
    print(f"Página actual: {historial[-1]}")


# ── Prueba ──────────────────────────────────────────────────
pagina_actual()
visitar("Google")
visitar("YouTube")
visitar("GitHub")
pagina_actual()
retroceder()
retroceder()
retroceder()
pagina_actual()