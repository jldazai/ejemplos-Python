# ejercicio funciones .74
def leer():
    numero = int(input("ingrese un numero: "))
    return numero
def mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
def menor(num1,num2):
    if num1 < num2:
        return num1
    else:
        return num2

numero1 = leer()
numero2 = leer()
maximo = mayor(numero1,numero2)
minimo = menor(numero1,numero2)
print("de los numeros ingresados {}, {}. el mayor es {} y el menor es {}".format(numero1,numero2,maximo,minimo))