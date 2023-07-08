import pandas as pd
import numpy as np
import scipy.stats as st

class Estimacion():
    def __init__(self,personas: pd.DataFrame):
        self.__personas_df = personas

    def estimate_norm_population_mean(self, column_name: str, alpha: float = 0.05):
        sample_mean = self.__personas_df[column_name].mean()
        sample_size = self.__personas_df.shape[0]

        #Distribución normal:
        # sample_mean es un estimador de la media poblacional (mu)
        pop_mean_estimation = sample_mean
        pop_var_estimation = (1/(sample_size - 1)) * sum((self.__personas_df[column_name] - sample_mean)**2)
        pop_std_estimation = pop_var_estimation ** 0.5
        M = st.norm.ppf(1 - alpha/2) * (pop_std_estimation / (sample_size ** 0.5))
        lower_limit = sample_mean - M
        upper_limit = sample_mean + M

        # Usar 4 decimales
        lower_limit = round(lower_limit, 4)
        pop_mean_estimation = round(pop_mean_estimation, 4)
        upper_limit = round(upper_limit, 4)

        return lower_limit, pop_mean_estimation, upper_limit

    def one_tail_test(self, column_name: str,year: int, test_against: float, alternative: str = 'lesser', alpha: float = 0.05) -> str:
        raise DeprecationWarning("Este método está deprecado, usar h_test")
    
        # 1er paso, elegir test the hipotesis
        test_h0 = "mu = {}".format(test_against)
        if alternative == 'lesser':
            test_h1 = "mu < {}".format(test_against)
        elif alternative == 'greater':
            test_h1 = "mu > {}".format(test_against)

        # 2do paso, definir criterio de rechazo
        if alternative == 'lesser':
            reject_h0 = lambda x, delta: x < (test_against - delta)
        elif alternative == 'greater':
            reject_h0 = lambda x, delta: x >= (test_against + delta)

        # Desviacion estandar de la muestra

        sample_std = self.__personas_df[(self.__personas_df['anio'] == year)][column_name].std()
        # Tamaño de la muestra
        sample_size = self.__personas_df.shape[0]
        # Media de la muestra
        sample_mean = self.__personas_df[(self.__personas_df['anio'] == year)][column_name].mean()

        # 3er paso, calcular estadistico de prueba
        delta = (-1 * sample_std) * (st.t.ppf(1 - alpha, df=(sample_size - 1))) / (sample_size ** 0.5)

        # 4to paso, tomar decision
        if reject_h0(sample_mean, delta):
            return f"Rechazar H0: {test_h0} a un nivel de significancia de {alpha}"
        else:
            return f"No se puede rechazar H0: {test_h0} a un nivel de significancia de {alpha}"

    def two_tail_test(self, column_name: str, test_against: float, alpha: float = 0.05) -> str:
        raise DeprecationWarning("Este método está deprecado, usar h_test")

        # 1er paso, elegir test the hipotesis
        test_h0 = "mu = {}".format(test_against)
        test_h1 = "mu != {}".format(test_against)

        # 2do paso, definir criterio de rechazo
        reject_h0 = lambda x, delta: (x < (test_against - delta)) or (x > (test_against + delta))

        # Desviacion estandar de la muestra
        sample_std = sample[column_name].std()
        # Tamaño de la muestra
        sample_size = sample.shape[0]
        # Media de la muestra
        sample_mean = sample[column_name].mean()

        # 3er paso, calcular estadistico de prueba
        delta = sample_std * (st.t.ppf(1 - alpha/2, df=(sample_size - 1))) / (sample_size ** 0.5)

        # 4to paso, tomar decision
        if reject_h0(sample_mean, delta):
            return f"Rechazar H0: {test_h0} a un nivel de significancia de {alpha}"
        else:
            return f"No se puede rechazar H0: {test_h0} a un nivel de significancia de {alpha}"
        
    def h_test(self, sample: pd.DataFrame, column_name: str, test_against: float | pd.DataFrame, alternative: str = 'less', alpha: float = 0.05) -> tuple[bool, float]:
        if alternative not in ['less', 'greater', 'two-sided']:
            raise ValueError("alternative must be 'less', 'greater' or 'two-sided'")
        if alpha <= 0 or alpha >= 1:
            raise ValueError("alpha must be between 0 and 1")
        if column_name not in sample.columns:
            raise ValueError("column_name must be in sample.columns")
        if isinstance(test_against, pd.DataFrame) and column_name not in test_against.columns:
            raise ValueError("column_name must be in test_against.columns")
        if isinstance(test_against, pd.DataFrame) and sample.shape[1] != test_against.shape[1]:
            raise ValueError("sample and test_against must have the same number of columns")

        # Get p-value
        if (isinstance(test_against, pd.DataFrame)):
            result = st.ttest_ind(sample[column_name], test_against[column_name], equal_var=False, alternative=alternative)
        else:
            result = st.ttest_1samp(sample[column_name], test_against, alternative=alternative)
        
        # Compare p-value with alpha
        if result.pvalue < alpha:
            return True, result.pvalue
        else:
            return False, result.pvalue