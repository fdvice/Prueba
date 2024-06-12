import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import time

# Inicializar Faker
fake = Faker()

# Medir el tiempo de inicio
start_time = time.time()

# Parámetros del dataset
n_samples = 10000

# Función para generar datos sintéticos usando Faker
def generate_synthetic_data(n_samples):
    data = []
    for _ in range(n_samples):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
        profile = fake.simple_profile()
        data.append([name, address, email, birthdate, profile['sex']])
    return pd.DataFrame(data, columns=['Name', 'Address', 'Email', 'Birthdate', 'Sex'])

# Generar datos sintéticos
df = generate_synthetic_data(n_samples)

# Medir el tiempo de finalización
end_time = time.time()
generation_time = end_time - start_time

# Visualización de la distribución de edades
def plot_age_distribution(df):
    df['Age'] = df['Birthdate'].apply(lambda x: 2024 - x.year)  # Asumimos el año actual es 2024
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title("Distribución de Edad")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

# Visualización de la distribución por sexo
def plot_sex_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sex', data=df)
    plt.title("Distribución por Sexo")
    plt.xlabel("Sexo")
    plt.ylabel("Frecuencia")
    plt.show()

# Mostrar información del dataset
print(f"Datos generados: {n_samples} muestras.")
print(f"Tiempo de generación: {generation_time:.4f} segundos.")
print(df.head())

# Llamar a la función de visualización de distribución de edades
plot_age_distribution(df)

# Llamar a la función de visualización de distribución por sexo
plot_sex_distribution(df)
