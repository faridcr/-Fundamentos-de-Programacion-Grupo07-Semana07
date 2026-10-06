
<<<<<<< HEAD
# Dada la cadena ' Python es divertido ', elimina los espacios en los extremos y cuenta cuántos caracteres tiene la
# cadena limpia

frase=" Python es divertido "
limpio=frase.strip()
limpio_inicio=frase.lstrip()
limpio_final=frase.rstrip()
sin_espacios=frase.replace(" ","")
print("La cadena limpia es      :",limpio)
print("Sin espacion al inicio es:",limpio_inicio)
print("sin espacio al final es  :",limpio_final)
print("sin espacios en blanco   :",sin_espacios)
print("tiene ", len(limpio), "caracteres")
=======
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



>>>>>>> e9002788af789dea3b8da7e4dbc57118f18cf537
