import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mimesis import Person, Address, Business
from mimesis.enums import Gender
import time

# Inicializar generadores de Mimesis
person = Person('en')
address = Address('en')
business = Business('en')

# Medir el tiempo de inicio
start_time = time.time()

# Parámetros del dataset
n_samples = 10000

# Función para generar datos sintéticos usando Mimesis
def generate_synthetic_data(n_samples):
    data = []
    for _ in range(n_samples):
        name = person.full_name(gender=Gender.MALE if np.random.rand() > 0.5 else Gender.FEMALE)
        addr = address.address()
        email = person.email()
        job = business.company()
        salary = business.price(minimum=30000, maximum=120000)
        data.append([name, addr, email, job, salary])
    return pd.DataFrame(data, columns=['Name', 'Address', 'Email', 'Company', 'Salary'])

# Generar datos sintéticos
df = generate_synthetic_data(n_samples)

# Medir el tiempo de finalización
end_time = time.time()
generation_time = end_time - start_time

# Visualización de la distribución de salarios
def plot_salary_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Salary'], bins=30, kde=True)
    plt.title("Distribución de Salarios")
    plt.xlabel("Salario")
    plt.ylabel("Frecuencia")
    plt.show()

# Visualización de la distribución de nombres por género
def plot_name_gender_distribution(df):
    df['Gender'] = df['Name'].apply(lambda x: 'Male' if 'Mr.' in x else 'Female')
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Gender', data=df)
    plt.title("Distribución por Género")
    plt.xlabel("Género")
    plt.ylabel("Frecuencia")
    plt.show()

# Mostrar información del dataset
print(f"Datos generados: {n_samples} muestras.")
print(f"Tiempo de generación: {generation_time:.4f} segundos.")
print(df.head())

# Llamar a la función de visualización de distribución de salarios
plot_salary_distribution(df)

# Llamar a la función de visualización de distribución por género
plot_name_gender_distribution(df)
