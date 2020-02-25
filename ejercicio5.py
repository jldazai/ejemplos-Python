#ejercicios con ciclos .31
inicio = int(input("ingrese el inicio del rango a sumar: "))
fin = int(input("ingrese el fin del rango a sumar: "))
suma = 0
for x in range(inicio, fin+1):
    suma = suma+x
print("la suma de los numero comprendidos entre {} y {} es: {}".format(inicio, fin, suma))