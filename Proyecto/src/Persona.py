
class Persona:
    def __init__(self, id, anio, mes, sexo, edad, region, pea, desempleo, salario):
        self.id = id
        self.anio = anio
        self.mes = mes
        self.sexo = sexo
        self.edad = edad
        self.region = region
        self.pea = pea
        self.desempleo = desempleo
        self.salario = salario
        # if ',' in salario:
        #     self.salario = float(salario.replace(',', '.'))
        # else:
        #     self.salario = float(salario)
            

    def __str__(self):
        return f"ID: {self.id}\nAño: {self.anio}\nMes: {self.mes}\nSexo: {self.sexo}\nEdad: {self.edad}\nRegión: {self.region}\nPEA: {self.pea}\nDesempleo: {self.desempleo}\nSalario: {self.salario}"