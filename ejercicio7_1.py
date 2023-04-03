from operacioness import suma, resta, dividir, multiplicar

a = 8
b = 4
rSuma = suma(a, b)
print("Para el calculo de las siguientes operaciones se usaron los valores de a = {} y b = {}.".format(a, b))
print("La suma de a y b es: ", rSuma)

rResta = resta(a, b)
print("La resta de a y b es: ", rResta)

rMulti = multiplicar(a, b)
print("La multiplicación de a y b es: ", rMulti)

rDiv = dividir(a, b)
print("La división de a y b es: ", int(rDiv))