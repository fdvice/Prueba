import numpy as np 
import pandas as pd 

#Comenzamos introduciendo los datos de los dos DataFrames
dataf1 = pd.DataFrame({
    'Nombre' : ['Jorge', 'Luis', 'Alberto', 'Maria', 'Abril'],
    'Edad' : [17,25,21,18,16]
})

dataf2 = pd.DataFrame({
    'Nombre' : ['Luis', 'Ana', 'Abril', 'Samuel', 'Maria'],
    'Peso' : [94,55,62,84,70]
})

print(dataf1)
print(dataf2)

#Union interna
outer_join = dataf2.merge(right=dataf1, how='inner', on='Nombre',indicator=True)
print(outer_join)

#Union externa
outer_join = dataf2.merge(right=dataf1, how='outer', on='Nombre',indicator=True)
print(outer_join)