import csv

class LectorCSV:
    def __init__(self, archivo):
        self.archivo = archivo
        self.datos = []

    def leer_archivo(self):
        with open(self.archivo, 'r') as archivo_csv:
            lector = csv.DictReader(archivo_csv, delimiter=';')
            for fila in lector:
                id = int(fila['ID'])
                anio = int(fila['anio'])
                mes = int(fila['mes'])
                sexo = int(fila['Sexo'])
                edad = int(fila['Edad'])
                region = int(fila['region'])
                pea = int(fila['PEA'])
                desempleo = int(fila['Desempleo'])
                salario = float(fila['Salario'])
                datos_persona = {
                    'ID': id,
                    'anio': anio,
                    'mes': mes,
                    'Sexo': sexo,
                    'Edad': edad,
                    'region': region,
                    'PEA': pea,
                    'Desempleo': desempleo,
                    'Salario': salario
                }
                self.datos.append(datos_persona)

    def obtener_datos(self):
        return self.datos

lector = LectorCSV('datos.csv')
lector.leer_archivo()
datos = lector.obtener_datos()

for persona in datos:
    print(persona)
