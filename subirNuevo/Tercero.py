import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_blobs, make_moons
import time

# Medir el tiempo de inicio
start_time = time.time()

# Parámetros del dataset
n_samples = 10000
n_features = 10
n_classes = 2
n_clusters_per_class = 2

# Generar datos sintéticos usando make_classification
X, y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=5, 
                           n_redundant=2, n_classes=n_classes, n_clusters_per_class=n_clusters_per_class, 
                           random_state=42)

# Convertir a DataFrame para facilidad de manejo
df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(n_features)])
df['class'] = y

# Medir el tiempo de finalización
end_time = time.time()
generation_time = end_time - start_time

# Comprobación de la distribución usando seaborn pairplot
def check_distribution(df):
    sns.pairplot(df, hue='class', palette='Set1', diag_kind='kde', plot_kws={'alpha':0.6})
    plt.show()

# Visualización de los datos
def plot_data_2d(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='feature_1', y='feature_2', hue='class', data=df, palette='Set1', alpha=0.6)
    plt.title("Datos Sintéticos (2D)")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.legend()
    plt.show()

# Mostrar información del dataset
print(f"Datos generados: {n_samples} muestras con {n_features} características cada una.")
print(f"Tiempo de generación: {generation_time:.4f} segundos.")

# Llamar a la función de comprobación de distribución
check_distribution(df)

# Llamar a la función de visualización 2D
plot_data_2d(df)
