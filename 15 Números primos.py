def esPrimo(numero):
    if numero<2:
        return False
    for i in range(2,numero):
        if numero%i == 0:
            return False
    else:
        print("\n"numero)

lista = []
for x in range(1,11):
    norteños = int(input())
    lista.append(norteños)
for s in lista:
    esPrimo (s)
