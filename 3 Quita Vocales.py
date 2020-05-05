vocales = "aeiouAEIOU"
espacios = "          "
cambia = str.maketrans(vocales,espacios)
oración = input()
sinvocales = oración.translate(cambia)
sinespacios = sinvocales.replace(" ","")
print(sinespacios)
