import csv
import os
from Persona import Persona
class LectorCSV:
    def __init__(self, path: str):
        # Obtener la ruta absoluta del programa
        actual_dir = os.path.dirname(os.path.abspath(__file__))
        # Unir la ruta del programa con la ruta del archivo
        self.archivo = os.path.join(actual_dir, path)
        self.datos: list[Persona] = []

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
                salario_str = fila['Salario'].replace(',', '.')  # Eliminar la coma
                salario = float(salario_str)  # Convertir a float
                self.datos.append(Persona(id, anio, mes, sexo, edad, region, pea, desempleo, salario))

    def obtener_datos(self) -> list[Persona]:
        return self.datos