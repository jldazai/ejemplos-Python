# ejercicio con cadenas .61
frase = input("ingrese una frase: ")
reves = ""
cont = len(frase) - 1
while cont >= 0:
    reves = reves + frase[cont]
    cont = cont - 1
print("su frase: {}\nal reves es: {}".format(frase,reves))