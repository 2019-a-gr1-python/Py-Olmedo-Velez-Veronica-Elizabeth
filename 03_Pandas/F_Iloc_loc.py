#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:36:32 2019

@author: VeronicaOlmedo
"""

import pandas as pd


path_guardado= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

#Filtrado de filas
#Devuelve toda la columna slice por fila label
primero = df.loc[1035]

#Acceder a la fila del artista solo con un label
primero = df.loc[1035]['artist']
primero = df.loc[1035,1]# no se puede sale un error
segundo = df.loc[1036,'units']

#Error por que no esta dentro del label indice
df.loc[0]

primero_a= df.iloc[0][1] #Son posiciones 

#Utilizar con rangos
primero_b= df.iloc[0,:]

primero_c= df.iloc[0,0:1]

primero_d= df.iloc[0,0:-2]

#Quiero de los primeros 100 aristas 
artist_100 = df.iloc[0:100,2:4]

#Ordenar
a= df['width'].sort_values()
a= df['width'].sort_values(axis=0)
b= df['heigth'].sort_values()


#Coger los 10 primeros
diez_primeros=df.head(10)['width'].sort_values(ascending=False).head(3)
diez_ultimos=df.head(10)['width'].sort_values().tail(3)

b = df['year'].sort_values(axis=0)

#Saber de todo el dataframe cuales son los que tienen mayor y menor width
serie_valido = pd.to_numeric(df['width'],errors='coerce') # Es una serie validada

df.loc[:,'width']=serie_valido
df.loc[:,5]=serie_valido


#Quiero 10 primera y la 10  ultimas que me digan las obras que tengan mayor ancho y mayor alto
diez_primero = df['width'].sort_values(ascending=False).head(10) #de mayor a menor

diez_ultimos = df['width'].sort_values(ascending=False).tail(10)


#Calcular el area el width por el heigth
#Limpiar los datos transformandolos a numeros 
serie_valido_height = pd.to_numeric(df['height'],errors='coerce')
df.loc[:,'height']=serie_valido_height 

area = df['height']*df['width']
type(area)

#Añadir una columna en el dataframe
df['area']=area

df=df.assign(aredos = area)

#Cual tien la mayor area
df_area=df['area'].sort_values(ascending=False).head(1)

id_max_area = df['area'].idxmax()

id_min_area = df['area'].idxmin()

#Registro con menor y mayor area
registro_mas_area = df.loc[id_max_area]
registro_menor_area = df.loc[id_min_area]





