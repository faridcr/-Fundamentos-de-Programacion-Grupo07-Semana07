#Enunciado5 –VALIDAR Y FORMATEAR CORRE ELECTRÓNICO

correo = input("Ingrese su correo electrónico: ").strip().lower()


print(f"\n-------CORREO ELECTRÓNICO ------\n")
if "@" not in correo or "." not in correo:
       print("Correo electronico inválido. Asegúrese de incluir '@' y '.' en la dirección ")

else:
      print(f"Correo electrónico valido : {correo}")


 