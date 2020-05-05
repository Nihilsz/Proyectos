import statistics
lista = []
estadisticas = int(input())
for i in range(1,estadisticas+1):
    numeros = int(input())
    lista.append(numeros)
print(lista)
print(statistics.mode(lista))
print(statistics.mean(lista))
print(statistics.stdev(lista))