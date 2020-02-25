# ejercicio recursividad 
# 79. Escribir una funcion recursiva que halle la suma de los primeros "n" numeros naurales
def sumar(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumar(numero-1)

num = int(input("ingrese un numero: "))
suma = sumar(num)
print("la suma de los {} pimeros numeros es {}".format(num,suma))