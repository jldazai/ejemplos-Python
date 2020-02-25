#ejercicio ciclo .34
par = 0
impar = 0
nume = 1
while nume != 0:
    nume = int(input("ingrese un numero diferente de cero: "))
    if nume % 2 == 0:
        par = par + abs(nume)
    else:
        impar = impar + abs(nume)
    print("la suma de los valores absolutos de los numeros pares ingresados es {}".format(par))
    print("la suma de los valores absolutos de los numeros impares ingresados es {}".format(impar))
print("fin del programa")