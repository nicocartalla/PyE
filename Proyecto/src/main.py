from LectorCSV import LectorCSV
from Persona import Persona
from EstadisticaDescriptiva import EstadisticaDescriptiva
import pandas as pd
import matplotlib.pyplot as plt


def main():
    lector = LectorCSV('../resources/ech_2022.csv')
    lector.leer_archivo()
    datos_personas: list[Persona] = lector.obtener_datos()
    
    ##################### Estadistica Descriptiva #####################
    ed = EstadisticaDescriptiva(datos_personas)
    ed.calcular_tasa_desempleo()
    ed.calcular_tasa_desempleo_por_rango_edad()
    ed.calcular_estadisticos_salarios()
    ed.imprimir_estadisticas_salarios()
    ed.generar_grafico()

if __name__ == '__main__':
    main()