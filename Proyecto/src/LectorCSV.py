import csv
import os
import pandas as pd
from Persona import Persona
class LectorCSV:
    def __init__(self, path: str):
        # Obtener la ruta absoluta del programa
        actual_dir = os.path.dirname(os.path.abspath(__file__))
        # Unir la ruta del programa con la ruta del archivo
        self.archivo = os.path.join(actual_dir, path)
        self.datos: list[Persona] = []
        self.encuesta: pd.DataFrame = None

    def leer_archivo(self):
        #with open(self.archivo, 'r') as archivo_csv:
        columnas = ["ID", "anio","mes","Sexo","Edad","region","PEA","Desempleo","Salario"]
        #encuesta = pd.read_csv("ech_2022.csv", usecols=columnas, delimiter=';')
        self.encuesta = pd.read_csv(self.archivo, usecols=columnas, delimiter=';')
        for _, row in self.encuesta.iterrows():
            persona = Persona(
                id=row["ID"],
                anio=row["anio"],
                mes=row["mes"],
                sexo=row["Sexo"],
                edad=row["Edad"],
                region=row["region"],
                pea=row["PEA"],
                desempleo=row["Desempleo"],
                salario=row["Salario"]
            )
            self.datos.append(persona)

    def obtener_datos(self) -> list[Persona]:
        return self.datos, self.encuesta