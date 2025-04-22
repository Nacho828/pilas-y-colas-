from ListaEnlazada import ListaEnlazada
from Nodo import Nodo

class RegistroMeteorologico:
    def __init__(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion

    def __str__(self):
        return f"Temperatura: {self.temperatura}°C, Humedad: {self.humedad}%, Presión: {self.presion} hPa"
