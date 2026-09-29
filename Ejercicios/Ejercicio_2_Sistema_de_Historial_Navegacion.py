historial = []

def visitar(url):
    historial.append(url)
    print("Visitando:", url)
    print("Historial:", historial)
    print("\n-----------------------\n")
    print()  


def retroceder():
    if len(historial) > 1:
        historial.pop()
        print("Regresaste a:", historial[-1])
    else:
        print("No puedes retroceder más")
    print()


def pagina_actual():
    if len(historial) > 0:
        print("Página actual:", historial[-1])
    else:
        print("No hay páginas en el historial")
    print()


visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()

pagina_actual()