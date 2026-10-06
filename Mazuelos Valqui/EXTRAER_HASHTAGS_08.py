# ---------- Extraer hashtags de un tweet ----------

tweet = "¡Qué partidazo! Vamos #Perú, hoy ganamos #Amistosos #VamosPerú #Mundial2026yafue!!"
hashtags = []
 
for palabra in tweet.split():
    if palabra.startswith("#"):
        hashtags.append(palabra[1:].strip(".,;:!?").lower())
 
print(sorted(hashtags))
