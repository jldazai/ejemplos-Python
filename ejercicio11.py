# ejercicio de fnciones .65
def potencia(base, expon):
    cont = 1
    pot = base
    while cont < expon:
        pot = pot*base
        cont = cont + 1
    return pot

num = int(input("ingrese la base: "))
expo = int(input("ingrese el exponente: "))
result = potencia(num,expo)
print("el numero {} elevado a la {} potencia es: {}".format(num,expo,result))

