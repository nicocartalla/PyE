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
    datos_persona_pea_df = datos_persona_df[datos_persona_df['PEA'] == 1]
    estimacion = Estimacion(datos_persona_pea_df)
    unemployment_estimation = estimacion.estimate_norm_population_mean('Desempleo')
    print("Intervalo de confianza")
    print(f"Limite inferior: {unemployment_estimation[0]}")
    print(f"Limite superior: {unemployment_estimation[2]}")
    print(f"Desempleo estimado: {unemployment_estimation[1]}")
    print("##############################################")
    ###################### HIPÓTESIS ######################
    print("---- Hipotesis ----")
    datos_persona_pea_2022_df = datos_persona_pea_df[datos_persona_pea_df['anio'] == 2022]
    rejected, p_value = estimacion.h_test(datos_persona_pea_2022_df, 'Desempleo', 0.07, 'greater')
    print(f"Aumento del desempleo en 2022? {rejected} (p-value: {p_value:.2e})")

    # Remover outliers
    data4 = datos_persona_pea_df[datos_persona_pea_df['Salario'] > 0]
    data4 = data4[data4['Salario'] < 150000]
    # Filtrar solo empleados
    data4 = data4[data4['Desempleo'] == 0] 
    # Separar por sexo
    data4_male = data4[data4['Sexo'] == 1]
    data4_female = data4[data4['Sexo'] == 2]

    # Test de hipótesis para diferencia de medias de salarios entre hombres y mujeres
    rejected, p_value = estimacion.h_test(data4_male, 'Salario', data4_female, 'two-sided', 0.01)
    print(f"Existe diferencia de medias de salarios entre hombres y mujeres? {rejected} (p-value: {p_value:.2e})")





if __name__ == '__main__':
    main()