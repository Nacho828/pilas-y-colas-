from ListaEnlazada import ListaEnlazada
from RegistroMeteorologico import RegistroMeteorologico


class EstacionMeteorologica:
    def __init__(self):
        self.registros = ListaEnlazada()

    def agregar_registro(self, temperatura, humedad, presion):
        registro = RegistroMeteorologico(temperatura, humedad, presion)
        self.registros.agregar(registro)

    def mostrar_registros(self):
        print("Registros meteorológicos:")
        self.registros.mostrar()