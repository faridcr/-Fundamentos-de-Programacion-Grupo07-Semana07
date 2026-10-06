
# Escribe una función que reciba un email, lo limpie (strip+lower), verifique que contiene '@' y '.' y retorne el dominio
def dominio(email):
    limpio=email.strip().lower()
    if '@' in limpio and '.' in limpio:
        return limpio.split('@')[1]
    else:
        return "Email inválido"
    
while True:
    email=input("ingrese su email:")
    resultado=dominio(email)
    if resultado=="Email inválido":
        print(resultado)
    else:
        print("El dominio del email es :", resultado)
        break