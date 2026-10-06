# ---------- Frecuencia de palabras ----------

def frecuencia_palabras(parrafo):
    stopwords = ["el", "la", "los", "las", "un", "una", "de", "y", "en", "es", "que", "a"]
 
    for signo in ".,;:!?¡¿()\"'":
        parrafo = parrafo.replace(signo, "")
 
    frecuencias = {}
    for palabra in parrafo.lower().split():
        if palabra not in stopwords:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias
 
parrafo = "Lima es una ciudad grande. En Lima hay playas, y los turistas visitan Lima para comer ceviche. ¡El ceviche es delicioso!"
print(frecuencia_palabras(parrafo))
 