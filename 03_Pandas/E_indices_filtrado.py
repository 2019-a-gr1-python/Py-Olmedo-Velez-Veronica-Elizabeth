#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:16:14 2019

@author: VeronicaOlmedo
"""


import pandas as pd


path_guardado= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

#Sacar alguna columna de dataframe

serie_artistas_duplicados = df_completo_pickle['artist']

#Cuantos artistas estan solitos
artistas = pd.unique(serie_artistas_duplicados)

artistas.size

len(artistas)


blake = df_completo_pickle['artist'] == 'Blake, William'
type(blake)  # pandas.core.series.Series

#Todas las obras del artista

#Cuantas obras de Blake tengo
blake.value_counts()

df_blake = df_completo_pickle[blake]


type(df_blake)
df_blake









































