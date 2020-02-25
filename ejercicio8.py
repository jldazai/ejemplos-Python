#ejercicios con estruturas .48
tupla = (25,789,45,69,23,2,15,548,1235,5874,545,55,332,15,9,134,201,564,95,78)
promPar = 0
promImpar = 0
for pos, nume in enumerate (tupla):
    if pos%2 == 0:
        promPar = promPar + nume
    else:
        promImpar = promImpar + nume
promPar = promPar / 10
promImpar = promImpar / 10
print("el promedio de los numeros en las posiciones pares es: {}".format(promPar))
print("el promedio de los numeros en las posiciones impares es: {}".format(promImpar))
