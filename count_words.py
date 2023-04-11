def contadorpalabras(palabras):
    diccionario_palabras = {}
    palabras = palabras.split()
    for pala in palabras:
        if pala in diccionario_palabras:
            diccionario_palabras[pala]=diccionario_palabras[pala]+1
        else:
            diccionario_palabras[pala]=1
    return diccionario_palabras