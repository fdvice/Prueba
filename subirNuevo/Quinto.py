import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, uniform, binom
from pydbgen import pydbgen
import time

# Inicializar Pydb
myDB = pydbgen.pydb()

# Medir el tiempo de inicio
start_time = time.time()

# Parámetros del dataset
n_samples = 10000

# Generar datos ficticios usando pydbgen
df_pydb = myDB.gen_dataframe(n_samples, fields=['name', 'city', 'phone', 'company', 'job_title'])

# Generar datos con distribución normal, uniforme y binomial usando scipy.stats
np.random.seed(42)
normal_data = norm.rvs(size=n_samples, loc=0, scale=1)
uniform_data = uniform.rvs(size=n_samples, loc=0, scale=10)
binomial_data = binom.rvs(n=10, p=0.5, size=n_samples)

# Crear un DataFrame combinado
df_stats = pd.DataFrame({
    'NormalDist': normal_data,
    'UniformDist': uniform_data,
    'BinomialDist': binomial_data
})

# Medir el tiempo de finalización
end_time = time.time()
generation_time = end_time - start_time

# Visualización de la distribución de los datos generados
def plot_distributions(df):
    plt.figure(figsize=(15, 5))
    for i, column in enumerate(df.columns, 1):
        plt.subplot(1, 3, i)
        sns.histplot(df[column], kde=True, bins=30)
        plt.title(f'Distribución de {column}')
    plt.tight_layout()
    plt.show()

# Mostrar información del dataset
print(f"Datos generados: {n_samples} muestras.")
print(f"Tiempo de generación: {generation_time:.4f} segundos.")
print(df_pydb.head())
print(df_stats.head())

# Llamar a la función de visualización de distribuciones
plot_distributions(df_stats)
