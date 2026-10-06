# ---------- Validar y formatear correo ----------

def procesar_email(email):
    email = email.strip().lower()
    if "@" in email and "." in email:
        return email.split("@")[1]   # dominio
    return "Email inválido"
 
print(procesar_email("  Josue.Mazuelos@Gmail.COM  "))   # gmail.com
print(procesar_email("correo-malo"))                 # Email inválido
