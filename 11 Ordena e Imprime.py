números = []
print("ingrese 3 números decimales menor a 10")
for i in range(1,4):
    decimal = float(input())
    números.append(decimal)
números.sort()
enteros={1:"uno",2:"dos",3:"tresh",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",10:"diez"}
print(enteros[int(números[-1])])
