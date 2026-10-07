# Ejercicio 8 - EXTRAER HASHTAGS DE UN TWEET

tweet = "Kevin estudia #Python y trabaja en #Lima hace #5 años"

hashtags = []

for palabra in tweet.split():
    if palabra.startswith("#"):
        hashtags.append(palabra[1:].lower())

hashtags.sort()

print(hashtags)
