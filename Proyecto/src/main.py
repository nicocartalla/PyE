from LectorCSV import LectorCSV
from Persona import Persona
from EstadisticaDescriptiva import EstadisticaDescriptiva
from Estimacion import Estimacion
# import pandas as pd
# import matplotlib.pyplot as plt


def main():
    lector = LectorCSV('../resources/ech_2022.csv')
    lector.leer_archivo()
    datos_personas: list[Persona] = lector.obtener_datos()[0]
    datos_persona_df = lector.obtener_datos()[1]
    
    ##################### Estadistica Descriptiva #####################
    ed = EstadisticaDescriptiva(datos_personas)
    ed.calcular_tasa_desempleo()
    ed.calcular_tasa_desempleo_por_rango_edad()
    ed.calcular_estadisticos_salarios()
    #ed.imprimir_estadisticas_salarios()
    ed.generar_grafico()

    ##################### Estimacion #####################
    print("##############################################")
    print("---- Estimacion ----")
    estimacion = Estimacion(datos_persona_df[datos_persona_df['PEA'] == 1])
    unemployment_estimation = estimacion.estimate_norm_population_mean('Desempleo')
    print("Intervalo de confianza")
    print(f"Limite inferior: {unemployment_estimation[0]}")
    print(f"Limite superior: {unemployment_estimation[2]}")
    print(f"Desempleo estimado: {unemployment_estimation[1]}")
    print("##############################################")
    ###################### HIPÓTESIS ######################
    print("---- Hipotesis ----")
    print("Mo aumento el desempleo en la poblacion de 2022 con respecto a 2021:", end=" ")
    print(estimacion.one_tail_test('Desempleo',2022, 0.07, 'greater', 0.05))

    salaries_without_outliers = datos_persona_df[(datos_persona_df['Salario'] > 0) & (datos_persona_df['Salario'] < 1000000)]
    data2 = salaries_without_outliers
    print("No existen diferencias significativas entre el salario promedio de hombres y mujeres:")
    estimacion_2 = Estimacion(data2[data2['PEA'] == 1 & (data2['Sexo'] == 2)]) 
    _, estimated_sex2_salary_mean, _ = estimacion_2.estimate_norm_population_mean('Salario')
    print(estimacion_2.two_tail_test(data2[data2['PEA'] == 1 & (data2['Sexo'] == 1)], 'Salario', estimated_sex2_salary_mean, 0.01))




if __name__ == '__main__':
    main()