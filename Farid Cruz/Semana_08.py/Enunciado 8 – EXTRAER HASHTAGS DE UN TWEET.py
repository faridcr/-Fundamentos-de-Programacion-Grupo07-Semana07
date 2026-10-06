# Ejercicio 8 - Extraer hashtags de un tweet
# Enunciado: Extraer los hashtags (#palabras) y devolverlos
# en una lista ordenada y en minúsculas.

# 1. Definir el tweet
tweet = "Aprendiendo #Python con el profe Percy #ProfePercy #Programacion #DataScience #python"

# 2. Lista vacía para guardar los hashtags
hashtags = []

# 3. Recorrer cada palabra del tweet
for palabra in tweet.split():
    # 4. Si empieza con '#', guardarla en minúsculas
    if palabra.startswith("#"):
        hashtags.append(palabra.lower())

# 5. Ordenar y mostrar
hashtags.sort()
print(hashtags)