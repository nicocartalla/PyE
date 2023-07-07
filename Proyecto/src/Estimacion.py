from Persona import Persona
import math
from matplotlib.ticker import FuncFormatter
#import statistics as st
import numpy as np
import scipy.stats as st
class Estimacion():
    def __init__(self,personas: list[Persona]):
        self.__personas = personas
        self.__personas_desempleadas = [ persona for persona in self.__personas if persona.pea == 1 and persona.edad >= 14 and persona.desempleo == 1]
        self.__personas_ocupadas = [persona for persona in self.__personas if persona.edad >= 14 and persona.desempleo == 2]
        self.__POBLACION = 1757161


    def desempleo_total_poblacion(self):
        #desempleo_estimado = (desempleados / tamaño_muestra) * tamaño_población
        desempleo_estimado = (len(self.__personas_desempleadas) / len(self.__personas)) * self.__POBLACION
        return desempleo_estimado
    
    def intervalo_de_confianza(self):
        pass

    def prueba_hipotesis_salarios(self):
        pass