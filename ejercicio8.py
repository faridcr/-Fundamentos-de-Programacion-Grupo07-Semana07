
# Dado un texto de tweet, extrae todos los hashtags (#palabras) y devuélvelos en una lista ordenada y en minúsculas.
def extraer_hashtags(texto):
    hashtags = []
    for palabra in texto.split():
        if palabra.startswith("#"):
            hashtags.append(palabra[1:].lower())
    return sorted(hashtags)

print("Ingrese el texto del tweet:")
tweet = input()
print("Hashtags encontrados:", extraer_hashtags(tweet)) 