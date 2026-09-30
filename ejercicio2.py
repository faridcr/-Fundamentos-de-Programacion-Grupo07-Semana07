
class historial_na:
    def __init__(self):
        self.pila=[]
        
    def visitar(self,pagina):
        self.pila.append(pagina)
        print("visitaste",pagina)
        
    def atras(self):
        if self.pila:
            pagina = self.pila.pop()
            print("retrocediste desde :", pagina)
        else:
            print("no hay historial para retroceder ")
    def mostrar_hostorial(self):
        if self.pila:
            print("historial de navegacion ")
            for pagina in reversed(self.pila):
                print("-", pagina)
        else:
            print("El historial esta vacio .")
            

historial=historial_na()

while True:
    print("Opciones :")
    print("1. visitar pagina ")
    print("2. Retroceder ")
    print("3. Mostrar Historial")
    print("4. Salir ")
    
    opcion=input("Elige una opcion : ")
    
    if opcion== "1":
        pagina=input("ingrese la pagina a visitar : ")
        historial.visitar(pagina)
    elif opcion== "2":
        historial.atras()
    elif opcion=="3":
        historial.mostrar_hostorial()
    elif opcion== "4":
        print("Saliendo del navegador ....")
        break
    else:
        print("opcion no validad intente de nuevo .")



