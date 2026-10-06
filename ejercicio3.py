class cola:
    def __init__(self):
        self.cola=[]
    
    def agregar(self,elemento):
        self.cola.append(elemento)
        print(elemento,"se agrego a la cola ")

    def atender(self):
        if self.cola:
            atendido=self.cola.pop(0)
            print("Fue atendido ",atendido)
        else:
            print("no hay ninguna cola ")
            
    def mostrar(self):
        if self.cola:
            print("elementos en la cola :", self.cola)
        else:
            print("La cola esta vacia ")
        
        
cola=cola()    
while True:
    print("----- Opcones -----")
    print("1. agregar a la cola :")
    print("2. atender " )
    print("3. Mostrar cola")
    print("4. Salir ")
    
    opcion=input("Eliga una opcion :")
    
    if opcion== "1":
        elemento=input("Ingrese el nombre o el dato :1")
        cola.agregar(elemento)
    elif opcion== "2":
        cola.atender()
    elif opcion== "3":
        cola.mostrar()
    elif opcion == "4":
        print("Saliendo del programa ")
        break
    else:
        print("Elija una opcion correcta ")