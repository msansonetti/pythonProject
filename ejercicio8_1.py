f = open('archivo.txt', 'w')
f.close()

f = open('archivo.txt', 'a')
f.write("mis_datos\n")
f.write("mis_datos_new\n")
f.close()
