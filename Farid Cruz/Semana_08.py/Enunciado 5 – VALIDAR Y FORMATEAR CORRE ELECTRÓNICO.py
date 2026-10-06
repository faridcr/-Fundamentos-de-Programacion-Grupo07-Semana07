# Ejercicio 5 - Validar y formatear correo electrónico
# Enunciado: Escribir una función que reciba un email, lo limpie (strip + lower),
# verifique que contiene '@' y '.' y retorne el dominio.

def obtener_dominio(email):
    # 1. Limpiar el email: quitar espacios en los extremos y pasar a minúsculas
    email = email.strip().lower()

    # 2. Verificar que tenga '@'
    if "@" in email:
        # 3. Separar por '@' y quedarnos con la parte de la derecha (el dominio)
        dominio = email.split("@")[1]

        # 4. Verificar que el DOMINIO tenga un '.'
        if "." in dominio:
            return dominio

    # Si falta la '@' o el '.' en el dominio, es inválido
    return "Email inválido"


# Programa principal: pedir el email y mostrar el resultado
correo = input("Ingresa tu email: ")
print(f"Dominio: {obtener_dominio(correo)}")