from LectorCSV import LectorCSV
from Persona import Persona
from EstadisticaDescriptiva import EstadisticaDescriptiva
from Estimacion import Estimacion
# import pandas as pd
# import matplotlib.pyplot as plt


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

    ##################### Estimacion #####################
    # estimacion = Estimacion(datos_personas)
    # print(f"Desempleo estimado: {estimacion.desempleo_total_poblacion()}")
    # print(f"Intervalo de confianza: {estimacion.intervalo_de_confianza()}")

if __name__ == '__main__':
    main()