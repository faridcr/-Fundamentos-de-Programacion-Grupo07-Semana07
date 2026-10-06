# Ejercicio 1 - Saludo personalizado
# Enunciado: Pedir al usuario su nombre y mostrar
# 'Hola, [NOMBRE]! Bienvenido al curso.' con el nombre en MAYÚSCULAS.
# Condición extra: el nombre solo puede contener letras.

# 1. Pedir el nombre al usuario
nombre = input("Ingresa tu nombre: ").strip()

# 2. Validar que solo tenga letras con isalpha()
if nombre.isalpha():
    # 3. Mostrar el saludo con el nombre en MAYÚSCULAS
    print(f"Hola, {nombre.upper()}! Bienvenido al curso.")
else:
    print("Error: solo se permiten letras.")