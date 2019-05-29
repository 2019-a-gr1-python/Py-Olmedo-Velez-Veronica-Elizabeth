#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:22:55 2019

@author: VeronicaOlmedo
"""

#Agrupamiento
import pandas as pd
import numpy as np
import math


path_guardado= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

#Saca una copy con los 2 artistas
seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado_ay = seccion_df.groupby('acquisitionYear')
df_agrupado_ay = seccion_df.groupby('artist')


type(df_agrupado_ay)

for acquisitionYear, registros in df_agrupado_ay:
    print(acquisitionYear)
    #print(registros)

#Llenar valores vacios
def llenar_valores_vacios(series):
    valores = series.values_counts()
    if (valores.empty):
        return series
    
    """   
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        print(valor)
        print(type(valor))
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    """
    nuevo_valor = series.fillna(valores.index[0])
    return nuevo_valor

#Agrupar df por el artistas en una lista
#Guardar los dataframe, creamos otro y lo devolvemos   
def transformar_df(df):
    df_artist = df.groupby('artist')
    arreglo_df_grupo = []

    for nombre_artista, registros_agrupados in df_artist:
        copia=registros_agrupados.copy()
        serie_medium = registros_agrupados['medium']
        serie_units = registros_agrupados['units']
        copia.loc[:,'medium'] = llenar_valores_vacios(serie_medium) #Material en el que fue echo la obra de arte
        copia.loc[:,'units'] = llenar_valores_vacios(serie_units)
        arreglo_df_grupo.append(copia)
        
        
    nuevo_df_transformado = pd.concat(arreglo_df_grupo)
    return nuevo_df_transformado
        
        
seccion_df_t = transformar_df(seccion_df)        
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

