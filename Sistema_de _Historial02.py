#Simula el historial de un navegador web usando una Pila (Stack). El usuario visita páginas y puede retroceder.

pila = []
 
def visitar(url):
    pila.append(url)
    print("Visitaste:", url, "| Pila:", pila)
 
def retroceder():
    if len(pila) > 1:
        pila.pop()
        print("Regresaste a:", pila[-1])
    else:
        print("No hay página anterior")
 
def pagina_actual():
    print("Página actual:", pila[-1] if pila else "Ninguna")
 
# d) Prueba
visitar("Google")
visitar("YouTube")
visitar("GitHub")
retroceder()
retroceder()
pagina_actual()