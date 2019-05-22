#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:54:04 2019

@author: VeronicaOlmedo
"""

import pandas as pd
import os

"""
Como cargar y leer un ccv
"""

# Permite leer de 3 lugares
# Archivos texto -> JSON, CVS, HTML, XML...
# Binary Files -> (asdasdasdasd)
# Relational Database

path= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.csv'

#Leer
df = pd.read_csv(
        path,
        nrows=5, #Cuantas filas
        usecols=['id','artist']
        )


columnas_a_usar = ['id','artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units']


 df_completo = pd.read_csv(
                path,
                usecols=columnas_a_usar,
                index_col='id')

#Guardar los datos un nuevo archivo
path_guardado= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'
df_completo.to_pickle(path_guardado)




df_completo_pickle = pd.read_pickle(path_guardado)

df_completo.shape
# Tiene 69201 Requistros















