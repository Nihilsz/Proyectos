lista = []
for i in range(1,11):
    numeros = input(f"Ingrese 10 números {i}: ")
    lista.append(numeros)
lista.sort()
lista.sort(reverse=True)
print(lista)
