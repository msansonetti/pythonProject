import pickle

class Vechiculo:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def getTipo(self):
        return f"Mi vehiculo es de tipo: {self.tipo}"

f = open('mis_vehiculos.bin', 'rb')
coche = pickle.load(f)
f.close()

print(coche.getTipo(), "y de color: ", coche.color)
