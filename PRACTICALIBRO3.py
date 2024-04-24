import pandas as pd
import matplotlib.pyplot as plt

#Cargamos los datos del congreso
df = pd.read_excel("02_201606_1.xlsx", header=5)
df.head()

#Agfrupamos los municipios por comunidad
grouped = df.groupby('Nombre de Comunidad')
grouped.size()

#Cargamos los datos del senado
df_senado = pd.read_excel("senado.xlsx", header=6)
df_senado.head()

# a) Representar gráficamente el porcentaje de votos para cada partido por comunidad autónoma
for comunidad in df['Nombre de Comunidad'].unique():
    df_comunidad = df[df['Nombre de Comunidad'] == comunidad].iloc[:, 13:].sum()
    #Como nos salen muchos partidos con pocos votos y no son visibles, vamos a agrupar todos en un grupo llamado otros
    # Calcular el porcentaje de votos para cada partido
    porcentaje_votos = df_comunidad / df_comunidad.sum() * 100
    
    # Agrupar los partidos con menos del 3% de los votos en la categoría "Otros"
    otros = porcentaje_votos[porcentaje_votos < 3].sum()
    porcentaje_votos = porcentaje_votos[porcentaje_votos >= 3]
    porcentaje_votos['Otros'] = otros
    
    porcentaje_votos.plot(kind='pie', autopct='%1.1f%%')  # Asumiendo que las columnas de los partidos empiezan en la columna 4
    plt.title(f'Porcentaje de votos por partido en {comunidad}')
    plt.show()


# b) Calcular la provincia con mayor participación de votantes
df['Participación'] = df['Votos válidos'] / df['Total censo electoral']
provincia_max_participacion = df.groupby('Nombre de Provincia')['Participación'].mean().idxmax()
participacion_max = df.groupby('Nombre de Provincia')['Participación'].mean().max()
print(f'La provincia con mayor participación es {provincia_max_participacion} con un porcentaje de participación del {participacion_max*100:.2f}%')


# c) Estimación de cómo quedaría el congreso cambiando el diseño de los distritos electorales actuales
total_votos = df.iloc[:, 13:].sum().sum()
escaños_totales = 350  # Asumiendo que hay 350 escaños en el Congreso
# Calculamos los votos totales por partido
votos_por_partido = df.iloc[:, 13:].sum()
# Asignamos escaños a cada partido de forma proporcional a sus votos
escaños_por_partido = (votos_por_partido / total_votos * escaños_totales).astype(int)

print(escaños_por_partido)


# d) Compara los datos de los resultados en el congreso y el senado para cada partido político por comunidad autónoma
for comunidad in df['Nombre de Comunidad'].unique():
    df_congreso_comunidad = df[df['Nombre de Comunidad'] == comunidad].iloc[:, 13:].sum()
    df_senado_comunidad = df_senado[df_senado['Nombre de Comunidad'] == comunidad].iloc[:, 13:].sum()
        # Filtrar partidos con menos de 10 votos en total
    df_congreso_comunidad = df_congreso_comunidad[df_congreso_comunidad >= 1000]
    df_senado_comunidad = df_senado_comunidad[df_senado_comunidad >= 1000]
    df_comparativa = pd.DataFrame({'Congreso': df_congreso_comunidad, 'Senado': df_senado_comunidad})
    # Limitar la gráfica a los partidos con más votos
    df_comparativa = df_comparativa[df_comparativa.sum(axis=1) > df_comparativa.sum(axis=1).quantile(0.75)]
    
    # Crear una gráfica de barras para cada partido
    ax = df_comparativa.plot(kind='bar', stacked=False)
    plt.title(f'Comparativa de votos en Congreso y Senado en {comunidad}')
    
    # Rotar las etiquetas del eje x para que sean más legibles
    plt.xticks(rotation=45)
    
    plt.show()