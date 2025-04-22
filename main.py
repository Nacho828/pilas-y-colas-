from EstacionMeteorologica import EstacionMeteorologica
from ListaEnlazada import ListaEnlazada
from Nodo import Nodo

# Ejemplo de uso
if __name__ == "__main__":
    estacion = EstacionMeteorologica()
    estacion.agregar_registro(25, 60, 1013, "Madrid")
    estacion.agregar_registro(22, 55, 1010, "Barcelona")
    estacion.agregar_registro(30, 70, 1008, "Sevilla")
    estacion.mostrar_registros()