#ejercicio con coleciones .44

lista = []
prom = 0
while len(lista) <5:
    nume = float(input("ingrese un numero: "))
    lista.append(nume)
for x in lista:
    prom = prom + x
prom = prom/5
print("la media de los numeros ingresados es: {}".format(prom))
