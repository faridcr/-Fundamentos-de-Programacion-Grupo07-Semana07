# Creamos una lista que utilizaremos como Pila (Stack)
# La última página que entra será la primera en salir.
pila = []


# Función para visitar una nueva página
def visitar(url):
    # Agregamos la página al final de la pila
    pila.append(url)

    # Mostramos la página que acabamos de visitar
    print("Visitando:", url)

    # Mostramos cómo queda actualmente la pila
    print("Pila actual:", pila)


# Función para retroceder a la página anterior
def retroceder():
    # Verificamos si la pila tiene páginas
    if len(pila) > 1:

        # Eliminamos la página actual
        pagina_saliente = pila.pop()

        # La última página que queda es la anterior
        print("Retrocediendo desde:", pagina_saliente)
        print("Ahora estás en:", pila[-1])

    else:
        # Si solo queda una página, no podemos retroceder
        print("No hay páginas anteriores.")


# Función para mostrar la página actual
def pagina_actual():
    # Verificamos que la pila no esté vacía
    if len(pila) > 0:

        # La página actual es el último elemento de la pila
        print("Página actual:", pila[-1])

    else:
        print("No hay ninguna página abierta.")


# Probamos el programa
visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()

pagina_actual()