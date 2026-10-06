# Ejercicio 6 - Censurar palabra en un texto
# Enunciado: Reemplazar cada palabra prohibida por asteriscos del mismo largo.

# 1. Texto y lista de palabras prohibidas
texto = "careverga, eres un cojudo y un malparido, pendejo, vete a la mierda, conchatumadre, puta madre"
prohibidas = ["conchatumadre", "puta", "madre", "careverga",
              "malparido", "pendejo", "cojudo", "mierda"]

# 2. Reemplazar cada palabra por asteriscos del mismo largo
for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

# 3. Mostrar el texto censurado
print(texto)