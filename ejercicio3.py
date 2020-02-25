#ejercicios con codicionales .17

numeUno = float(input("ingrese un primer numero: "))
numeDos = float(input("ingrese un segundo numero: "))
numeTrs = float(input("ingrese un tercer numero: "))

if numeTrs >= numeDos:
    if numeDos >= numeUno:
        print("los numeros {}, {} y {} fueron ingresados en orden ascendente".format(numeUno,numeDos,numeTrs))
    else:
        print("los numeros no fueron ingresados en orden ascendente")
else:
    print("los numeros no fueron ingresados en orden ascendente")