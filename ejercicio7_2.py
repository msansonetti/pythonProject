import time

fecha = time.localtime()
hora = fecha.tm_hour
minutos = fecha.tm_min


if hora >= 19:
    print("Son las {} ¡Es la hora de irse a casa!".format(hora))
else:
    print("¡Aun te faltan {} hrs y {} minutos para irte a casa!".format(18 - int(hora), 59 - fecha.tm_min))
