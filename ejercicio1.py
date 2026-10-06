
#Pide al usuario su nombre y muestra: 'Hola, [NOMBRE]! Bienvenido al curso.' El nombre debe aparecer en
#MAYÚSCULAS
def dato(pedirdato):
    while True:
        nombre=input(pedirdato).strip()
        if nombre.isdigit():
                print("ingrese un nombre valido ")
                
        else:
            print(f"Hola, {nombre.upper()} Bienvenido al curso.")
            break
    
print("Bienvenido al programa de bienvenida")
print(dato("ingrese su nombre : "))