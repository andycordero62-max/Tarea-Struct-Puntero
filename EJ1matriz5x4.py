import numpy 

class EstructuraMatriz:
    def __init__(self, filas, columnas):
        self.datos = numpy.random.randint(1, 101, size=(filas, columnas))

mi_matriz = EstructuraMatriz(5, 4)
print("Matriz 5x4 creada dentro de una Clase:")
print(mi_matriz.datos)