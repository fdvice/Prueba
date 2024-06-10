import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import norm

# Función para generar datos sintéticos con distribución normal
def generate_synthetic_data(n_samples_per_class, n_features, means, stds):
    data = []
    labels = []
    for class_label, (mean, std) in enumerate(zip(means, stds)):
        class_data = np.random.normal(loc=mean, scale=std, size=(n_samples_per_class, n_features))
        data.append(class_data)
        labels.append(np.full(n_samples_per_class, class_label))
    return np.vstack(data), np.concatenate(labels)

# Medir el tiempo de inicio
start_time = time.time()

# Parámetros del dataset
n_samples_per_class = 10000
n_features = 5
n_classes = 2

# Medias y desviaciones estándar para cada clase y característica
means = [np.linspace(0, 10, n_features), np.linspace(10, 20, n_features)]
stds = [np.ones(n_features), np.ones(n_features)]

# Generar datos sintéticos
X, y = generate_synthetic_data(n_samples_per_class, n_features, means, stds)

# Medir el tiempo de finalización
end_time = time.time()
generation_time = end_time - start_time

# Comprobación de la distribución
def check_distribution(X, y, means, stds):
    fig, axes = plt.subplots(n_features, n_classes, figsize=(15, 10))
    for i in range(n_features):
        for j in range(n_classes):
            feature_data = X[y == j][:, i]
            axes[i, j].hist(feature_data, bins=50, density=True, alpha=0.6, color='g')
            xmin, xmax = axes[i, j].get_xlim()
            x = np.linspace(xmin, xmax, 100)
            p = norm.pdf(x, means[j][i], stds[j][i])
            axes[i, j].plot(x, p, 'k', linewidth=2)
            title = f'Clase {j} - Característica {i + 1}'
            axes[i, j].set_title(title)
    plt.tight_layout()
    plt.show()

# Visualización de los datos
def plot_data_2d(X, y):
    plt.figure(figsize=(10, 6))
    for class_label in np.unique(y):
        plt.scatter(X[y == class_label][:, 0], X[y == class_label][:, 1], label=f"Clase {class_label}", alpha=0.6)
    plt.title("Datos Sintéticos (2D)")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.legend()
    plt.show()

# Mostrar información del dataset
print(f"Datos generados: {n_samples_per_class * n_classes} muestras con {n_features} características cada una.")
print(f"Tiempo de generación: {generation_time:.4f} segundos.")

# Llamar a la función de comprobación de distribución
check_distribution(X, y, means, stds)

# Llamar a la función de visualización 2D
plot_data_2d(X, y)
