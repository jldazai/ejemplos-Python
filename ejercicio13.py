# ejercicio recursividad 
#78. escribir un programa que usando recursividad calcule el producto de
#dos enteros usando sumas succesivas
def multiplicar(numA, numB):
    if numB == 0:
        return 0
    elif numB == 1:
        return numA
    else:
        return numA + multiplicar(numA,numB-1)
    
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
mult = multiplicar(num1,num2)
print("el numero {} por el numero {} es {}".format(num1,num2,mult))

