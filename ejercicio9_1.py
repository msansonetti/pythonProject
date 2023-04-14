list_paises = input("Escriba los paises separados por comas: \n")

paises = [pais for pais in list_paises.split(",")]
paises = sorted(set(list_paises))

print("La lista de paises es: ", list_paises)
