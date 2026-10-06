# ---------- Validar y formatear correo ----------

def procesar_email(email):
    email = email.strip().lower()
    if "@" in email:
        dominio = email.split("@")[1]
        if "." in dominio:
            return dominio
    return "Email inválido"
