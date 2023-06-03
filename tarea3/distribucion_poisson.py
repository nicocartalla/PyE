import numpy as np
import statistics as st
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Parámetro de la distribución binomial
l = 30

# Tamaños de muestra
sample_sizes = [10**2, 10**3, 10**4, 10**5]

# Almacenar los valores calculados por cada tamaño de muestra
expecteds = []
medians = []
means = []
modes = []
variance_teos = []
variance_empis = []

# Funcion para calcular la varianza empirica
def variance_e(mean, sample):
    sum = 0
    for i in range(len(sample)):
        sum += (sample[i] - mean)**2
    return sum/(len(sample))

# Arreglo de figuras
fig, axs = plt.subplots(4,2)

# Título de la figura
fig.suptitle('Distribución Poisson de parámetro λ = '+ str(l))


for i, size in enumerate(sample_sizes):
    # Muestra
    sample = poisson.rvs(l, size=size)
    # Mediana
    median = np.median(sample)
    # Media
    mean = np.mean(sample)
    # Moda
    mode = st.mode(sample)
    # Varianza teorica
    variance_teo = l
    # Varianza empirica
    variance_empi = variance_e(mean, sample)
    # Esperanza
    expected = l
    
    medians.append(median)
    means.append(mean)
    modes.append(mode)
    variance_teos.append(variance_teo)
    variance_empis.append(variance_empi)
    expecteds.append(expected)

    # Diagrama de cajas
    axs[i, 0].boxplot(sample)
    axs[i, 0].set_ylabel('Valor')
    axs[i, 0].set_title('Diagrama de Cajas - Tamaño de Muestra: ' + str(size) )

    # Histograma
    axs[i, 1].hist(sample, bins=range(max(sample)+2), density=True, alpha=0.5)
    axs[i, 1].set_xlabel('Valor')
    axs[i, 1].set_ylabel('Frecuencia')
    axs[i, 1].set_title('Histograma - Tamaño de Muestra: ' + str(size))

# Ajustar los márgenes entre las subtramas
plt.tight_layout()
plt.subplots_adjust(hspace=0.8)

# Abrir la figura en pantalla completa
figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

# Mostrar la figura con los gráficos
plt.show()

# Imprimir Tamaño muestra, mediana, moda y esperanzas en consola
for i, size in enumerate(sample_sizes):
    texto = '------- Distribución Poisson de parámetro λ = '+ str(l) +' -------' + '\n' \
        + 'Tamaño de Muestra: ' + str(size) + '\n' \
        + 'Mediana: ' + str(medians[i]) + '\n' \
        + 'Media: ' + str(means[i]) + '\n' \
        + 'Moda: ' + str(modes[i]) + '\n' \
        + 'Varianza Teorica: ' + str(variance_teos[i]) + '\n' \
        + 'Varianza Empírica: ' + str(round(variance_empis[i],2)) + '\n' \
        + 'Esperanza: ' + str(expecteds[i]) + '\n' \
        + '-------------------------' + '\n'
    print(texto)
