# Ejercicio 9 - Analizar frecuencia de palabras
# Enunciado: Escribir una función que reciba un párrafo y retorne un diccionario
# con la frecuencia de cada palabra, ignorando signos de puntuación,
# mayúsculas y palabras vacías (stopwords).

# Palabras vacías: palabras comunes que no aportan información
stopwords = ["es", "un", "y", "se", "en", "el", "la", "de"]

def frecuencia_palabras(parrafo):
    # 1. Pasar todo a minúsculas
    texto = parrafo.lower()

    # 2. Quitar los signos de puntuación con replace()
    for signo in [".", ",", ";", ":", "!", "?", "¡", "¿"]:
        texto = texto.replace(signo, "")

    # 3. Crear el diccionario vacío donde se contarán las palabras
    frecuencias = {}

    # 4. Separar el texto en palabras y recorrerlas
    for palabra in texto.split():
        # 5. Ignorar las palabras vacías
        if palabra not in stopwords:
            # 6. Si ya existe en el diccionario, sumar 1; si no, empezar en 1
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1

    # 7. Devolver el diccionario
    return frecuencias


# Programa principal
parrafo = ("Python es genial. Python es un lenguaje muy útil, y Python se usa en datos.")
print(frecuencia_palabras(parrafo))