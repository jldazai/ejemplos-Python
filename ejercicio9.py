#cadenas de caracteres .56
cadena1 = "¡hola mundo! ¿que tal todo?"
cadena2 = ""
for letra in cadena1:
    if not letra == " ":
        cadena2 = cadena2 + letra
    
print("la cadena original es {}. \nla cadena sin espacios {}".format(cadena1,cadena2))
