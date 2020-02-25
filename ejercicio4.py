#ejercicios con codicionales .21
dia = int(input("ingrese el numero del dia correspondiene a la semana: "))
if dia == 1:
    print("el dia {} es el lunes".format(dia))
elif dia == 2:
    print("el dia {} es el martes".format(dia))
elif dia == 3:
    print("el dia {} es el miercoles".format(dia))
elif dia == 4:
    print("el dia {} es el jueves".format(dia))
elif dia == 5:
    print("el dia {} es el viernes".format(dia))
elif dia == 6:
    print("el dia {} es el sabado".format(dia))
elif dia == 7:
    print("el dia {} es el domingo".format(dia))
else:
    print("el numero {} no correspode a ningun dia de la semana".format(dia))
