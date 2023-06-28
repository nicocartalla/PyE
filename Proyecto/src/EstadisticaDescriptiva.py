from Persona import Persona
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import pandas as pd
import statistics

class EstadisticosSalarios():
    def __init__(self):
        self.media: float = 0.0
        self.mediana: float = 0.0
        self.moda: float = 0.0
        self.minimo: float = 0.0
        self.maximo: float = 0.0
        self.cuartil_1: float = 0.0
        self.cuartil_2: float = 0.0
        self.cuartil_3: float = 0.0


class EstadisticaDescriptiva():

    #Estadistica Descriptiva
    def __init__(self, datos: list[Persona]):
        self.__personas = datos
        self.__rangos_edad = {'14-17': (14, 17),
               '18-25': (18, 25),
               '26-40': (26, 40),
               'más de 40 años': (41, 150)}
        self.__tasa_desempleo = 0.0
        self.__tasa_desempleo_edad = {}
        self.__salarios = [persona.salario for persona in self.__personas]
        self.__estadisticos_salarios: EstadisticosSalarios = EstadisticosSalarios()

    #Tasa de desempleo
    def calcular_tasa_desempleo(self) -> float:

        total_personas = len(self.__personas)
        desemplados = sum( 1 for persona in self.__personas if persona.desempleo == 1)
        self.__tasa_desempleo = (desemplados / total_personas) * 100
        return self.__tasa_desempleo

    #Tasa de desempleo por rango de edad
    def calcular_tasa_desempleo_por_rango_edad(self) -> dict:

        for rango, (edad_min, edad_max) in self.__rangos_edad.items():
            desempleo_edad = len([persona for persona in self.__personas if persona.desempleo == 1 and edad_min <= persona.edad <= edad_max])
            self.__tasa_desempleo_edad[rango] = (desempleo_edad / len(self.__personas)) * 100

        return self.__tasa_desempleo_edad

    def calcular_estadisticos_salarios(self) -> EstadisticosSalarios:
        self.__estadisticos_salarios.media = statistics.mean(self.__salarios)
        self.__estadisticos_salarios.mediana = statistics.median(self.__salarios)
        self.__estadisticos_salarios.moda = statistics.mode(self.__salarios)
        self.__estadisticos_salarios.minimo = min(self.__salarios)
        self.__estadisticos_salarios.maximo = max(self.__salarios)
        self.__estadisticos_salarios.cuartil_1 = np.quantile(self.__salarios, 0.25)
        self.__estadisticos_salarios.cuartil_2 = np.quantile(self.__salarios, 0.5)
        self.__estadisticos_salarios.cuartil_3 = np.quantile(self.__salarios, 0.75)

        return self.__estadisticos_salarios
    
    def get_tasa_desempleo(self) -> float:
        return self.__tasa_desempleo

    def get_tasa_desempleo_edad(self) -> dict:
        return self.__tasa_desempleo_edad        

    def generar_grafico(self) -> None:
        fig, axs = plt.subplots(2, 3, figsize=(10, 10))

        # #Gráfico de barras para tasa de desempleo por rango de edad
        axs[0,0].bar(self.__tasa_desempleo_edad.keys(), self.__tasa_desempleo_edad.values())
        axs[0,0].set_xlabel('Rango de Edad')
        axs[0,0].set_ylabel('Tasa de Desempleo (%)')
        axs[0,0].set_title('Tasa de Desempleo por Rango de Edad')
        
        # # Histograma de salarios
        # Filtrar valores no válidos (negativos o cero)
        salarios_validos = [x for x in self.__salarios if x > 0]

        salarios_log = np.log10(salarios_validos)

        # Crear el histograma con la escala logarítmica en el eje x
        axs[0,1].hist(salarios_log, bins=50, edgecolor='black')

        # Configurar etiquetas y título del gráfico
        axs[0,1].set_xlabel('Salario')
        axs[0,1].set_ylabel('Frecuencia')
        axs[0,1].set_title('Histograma de Salarios')

        # Creo un formato personalizado para el eje x 
        # y aplico leyenda exponencial para numeros mayores a 6 cifras
        def log_scale_formatter(x, pos):
            if x >= 6:
                return '$10^{}$'.format(int(x))
            else:
                return int(10**x)

        # Crear el formateador personalizado y aplicarlo al eje x
        formatter = FuncFormatter(log_scale_formatter)
        axs[0,1].xaxis.set_major_formatter(formatter)
        #axs[0,1].gca().xaxis.set_major_formatter(formatter)
        
        # Cuando se hace zoom permitir que el eje x se ajuste automáticamente
        axs[0,1].autoscale(enable=True, axis='x')
        

        # Box-Plot de salarios
        axs[0,2].boxplot(salarios_log)
        axs[0,2].set_ylabel('Logaritmo del Salario')
        axs[0,2].set_title('Box-Plot de Salarios')
        axs[0,2].autoscale(enable=True, axis='x')

        # Boxplot por género
        #Salarios diferenciados por género
        salarios_masculino = [persona.salario for persona in self.__personas if persona.sexo == 1]
        salarios_masculino_log = np.log10([x for x in salarios_masculino if x > 0])
        salarios_femenino = [persona.salario for persona in self.__personas if persona.sexo == 2]
        salarios_femenino_log = np.log10([x for x in salarios_femenino if x > 0])

        #axs[1,0].figure(figsize=(8, 6))
        axs[1,0].boxplot([salarios_masculino_log, salarios_femenino_log], labels=['Masculino', 'Femenino'])
        axs[1,0].set_xlabel('Género')
        axs[1,0].set_ylabel('Salario')
        axs[1,0].set_title('Box-Plot de Salarios por Género')
        
        # Boxplot por zona geográfica
        # Salarios diferenciados por zona geográfica
        salarios_interior = [persona.salario for persona in self.__personas if persona.region == 1]
        salarios_interior_log = np.log10([x for x in salarios_interior if x > 0])
        salarios_montevideo = [persona.salario for persona in self.__personas if persona.region == 2]
        salarios_montevideo_log = np.log10([x for x in salarios_montevideo if x > 0])

        
        #axs[1,1].figure(figsize=(8, 6))
        axs[1,1].boxplot([salarios_interior_log, salarios_montevideo_log], labels=['Interior', 'Montevideo'])
        axs[1,1].set_xlabel('Zona Geográfica')
        axs[1,1].set_ylabel('Salario')
        axs[1,1].set_title('Box-Plot de Salarios por Zona Geográfica')
        axs[1,1].autoscale(enable=True, axis='x')

        # mostrar el texto de estadisticas de salarios en la ultima figura centrado
        texto = self.__get_texto_estadisticas_salarios()
        
        axs[1,2].text(0.5, 0.5, texto, fontsize=14, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round',pad=0.5), ha='center', va='center')

        axs[1,2].axis('off')


        plt.tight_layout()
        plt.show()

    def __get_texto_estadisticas_salarios(self):
        self.calcular_estadisticos_salarios()
        texto = "Estadisticas de Salarios\n" \
                + "-------------------------\n" \
                + "Media: " + str(self.__estadisticos_salarios.media) + "\n" \
                + "Mediana: " + str(self.__estadisticos_salarios.mediana) + "\n" \
                + "Moda: " + str(self.__estadisticos_salarios.moda) + "\n" \
                + "Minimo: " + str(self.__estadisticos_salarios.minimo) + "\n" \
                + "Maximo: " + str(self.__estadisticos_salarios.maximo) + "\n" \
                + "Cuartil 1: " + str(self.__estadisticos_salarios.cuartil_1) + "\n" \
                + "Cuartil 2: " + str(self.__estadisticos_salarios.cuartil_2) + "\n" \
                + "Cuartil 3: " + str(self.__estadisticos_salarios.cuartil_3) + "\n"
        return texto

    def imprimir_estadisticas_salarios(self):

        print("Estadisticas de Salarios")
        print("Media: ", self.__estadisticos_salarios.media)
        print("Mediana: ", self.__estadisticos_salarios.mediana)
        print("Moda: ", self.__estadisticos_salarios.moda)
        print("Minimo: ", self.__estadisticos_salarios.minimo)
        print("Maximo: ", self.__estadisticos_salarios.maximo)
        print("Cuartil 1: ", self.__estadisticos_salarios.cuartil_1)
        print("Cuartil 2: ", self.__estadisticos_salarios.cuartil_2)
        print("Cuartil 3: ", self.__estadisticos_salarios.cuartil_3)