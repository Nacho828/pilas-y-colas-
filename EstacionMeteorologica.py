class EstacionMeteorologica:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, temperatura, humedad, presion, region):
        registro = {
            "temperatura": temperatura,
            "humedad": humedad,
            "presion": presion,
            "region": region
        }
        self.registros.append(registro)

    def mostrar_registros(self):
        for registro in self.registros:
            print(f"Región: {registro['region']}, Temperatura: {registro['temperatura']}°C, Humedad: {registro['humedad']}%, Presión: {registro['presion']} hPa")