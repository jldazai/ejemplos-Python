# 
import time
def aSegundos(hora,minu,sec):
    hora = hora*3600
    minu = minu*60
    
    return (hora+minu+sec)

def aHoras(sec):
    hor = int(sec/3600)
    mint = int((sec-(hor*3600))/60)
    seg = sec-((hor*3600)+(mint*60))
    return [hor,mint,seg]
    
hora = int(input("ingrese las horas: "))
minu = int(input("ingrese los minutos: "))
sec = int(input("ingrese los segundos: "))

tiempo = aSegundos(hora,minu,sec)

while tiempo >= 0:
    tiempos = aHoras(tiempo)
    print("{}:{}:{}".format(tiempos[0],tiempos[1],tiempos[2]))
    tiempo = tiempo-1
    time.sleep(1)
    
print("tiempo finalizado")

