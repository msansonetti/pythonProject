class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.c = color
        self.r = ruedas
        self.p = puertas


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada):
        super().__init__(color="azul", ruedas=4, puertas=4)
        self.v = velocidad
        self.cc = cilindrada

    def __str__(self):
        return "Mi vehiculo es un coche de color {}, tiene {} ruedas y es de {} puertas. Alcanza una velocidad de {} km/h y una cilindrada de {} cc.".format(self.c, self.r, self.p, self.v, self.cc)


mi_coche = Coche(120, 1600)
print(mi_coche)
