import numpy as np
import scipy.stats as st
from scipy.stats import geom

import matplotlib.pyplot as plt

# Parámetros de la distribución geométrica
p = 0.08
sample_sizes = [10**2, 10**3, 10**4, 10**5]

# Generar muestras aleatorias y calcular la mediana y la moda
expecteds = []
medians = []
means = []
modes = []
variance_teos = []
variance_empis = []

def variance_e(mean, sample):
    sum = 0
    for i in range(len(sample)):
        sum += (sample[i] - mean)**2
    return sum/(len(sample))

fig, axs = plt.subplots(len(sample_sizes), 2, figsize=(10, 4*len(sample_sizes)))

for i, size in enumerate(sample_sizes):
    sample = geom.rvs(p, size=size)
    median = np.median(sample)
    mean = np.mean(sample)
    mode = st.mode(sample)
    variance_teo = (1-p)/(p**2)
    variance_empi = variance_e(mean, sample)
    expected = (1/p) - 1
    
    medians.append(median)
    means.append(mean)
    modes.append(mode)
    variance_teos.append(variance_teo)
    variance_empis.append(variance_empi)
    expecteds.append(expected)

    # Diagrama de cajas
    axs[i, 0].boxplot(sample)
    #axs[i, 0].set_xlabel('Tamaño de Muestra: ' + str(size))
    axs[i, 0].set_ylabel('Valor')
    axs[i, 0].set_title('Diagrama de Cajas')

    # Histograma
    axs[i, 1].hist(sample, bins=range(max(sample)+2), density=True, alpha=0.5)
    #axs[i, 1].set_xlabel('Valor')
    axs[i, 1].set_ylabel('Frecuencia')
    axs[i, 1].set_title('Histograma - Tamaño de Muestra: ' + str(size))

    # Agregar texto a la derecha de la gráfica
    texto = 'Tamaño de Muestra: ' + str(size) + '\n' \
            + 'Mediana: ' + str(median) + '\n' \
            + 'Media: ' + str(mean) + '\n' \
            + 'Moda: ' + str(mode) + '\n' \
            + 'Varianza Teorica: ' + str(variance_teo) + '\n' \
            + 'Varianza Empírica: ' + str(variance_empi) + '\n' \
            + 'Esperanza: ' + str(expected) + '\n' \
            + '-------------------------'
    #fig.text(0.75, 0.5, texto, fontsize=10)
    #axs[i, 1].text(1.05, 0.5, texto, fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

    # Ajustar los márgenes entre las subtramas
    plt.tight_layout()

# Mostrar la figura con los gráficos
plt.show()

# Imprimir medianas y modas
for i in range(len(sample_sizes)):
    print('Tamaño de Muestra:', sample_sizes[i])
    print('Mediana:', medians[i])
    print('Media:', means[i])
    print('Moda:', modes[i])
    print('Varianza Teorica:', variance_teos[i])
    print('Varianza Empírica:', variance_empis[i])
