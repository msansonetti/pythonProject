class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprime(self):
        print(f"El Alumno: {self.nombre}.")

    def aprobar(self):
        if self.nota >= 5:
            print(f"Ha obtenido una nota de: {self.nota}. Por lo tanto ha APROBADO.")
        else:
            print(f"Ha obtenido una nota de: {self.nota}. Por lo tanto ha REPROBADO.")


alu1 = Alumno("Juan Rodriguez", 7)
alu2 = Alumno("Miguel Pérez", 4)

alu1.imprime()
alu1.aprobar()

alu2.imprime()
alu2.aprobar()
