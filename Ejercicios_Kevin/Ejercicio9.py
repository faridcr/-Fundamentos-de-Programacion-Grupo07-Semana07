#Enunciado9 –ANALIZAR FRECUENCIA DE PALABRAS



def frecuencia_palabras(texto):
    texto = texto.lower()
    texto = texto.replace ("." , "")
    texto = texto.replace ("," , "")
    texto = texto.split()

    frecuencia = {}
    stopwords = ["el", "la", "de", "y", "es"]
    for palabra in texto:
        if palabra not in stopwords:
            if palabra in frecuencia:
                frecuencia[palabra] = frecuencia[palabra] + 1
            else: 
              frecuencia[palabra] = 1
    return frecuencia
texto = "Python es fácil, Python es divertido."

print(frecuencia_palabras(texto))



