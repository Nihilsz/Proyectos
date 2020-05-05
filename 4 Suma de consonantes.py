vocales = "aeiouAEIOU"
espacios = "          "
cambia = str.maketrans(vocales,espacios)
ingreseoración = input()
cambio = ingreseoración.translate(cambia)
sinvocales = cambio.replace(" ","")
suma = " ".join(sinvocales)
print(suma)
consonantes = len(suma.split())
print(consonantes)
