class Neurona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

capa_entrada = [Neurona("Pixel_1"), Neurona("Pixel_2")]
capa_oculta = [Neurona("H1"), Neurona("H2"), Neurona("H3")]
capa_salida = [Neurona("Gato"), Neurona("Perro")]

for n_entrada in capa_entrada:
    n_entrada.conexiones = capa_oculta 

for n_oculta in capa_oculta:
    n_oculta.conexiones = capa_salida

print(f"¿La conexión es una referencia válida?: {capa_entrada[0].conexiones is capa_oculta}")
print(f"Nombre de la neurona de salida: {capa_entrada[0].conexiones[0].conexiones[0].nombre}")