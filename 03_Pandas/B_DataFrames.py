#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:37:12 2019

@author: VeronicaOlmedo
"""

import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)

"""
DataFrame es un conjunto de series
Crear DataFrame tenemos mas columnas
"""

df = pd.DataFrame (arr_rand)

df1 = pd.DataFrame (
                    arr_rand,
                    columns =['Estatura(cm)','Peso(gr)','Edad (anios)']
                   )

"""
Las columnas se pueden integrar despues
Los indices tambien pueden ingresados despues
"""

df2 = pd.DataFrame (arr_rand)


df2.columns =  ['Estatura(cm)','Peso(gr)','Edad (anios)']
df2.index =['Adrian','Nika']

df3[O] #No es el indice es el nombre de la columna

df2['Estatura(cm)'] #Nombre de la columna

df2['Estatura(cm)'][0] # Para saber el indice


"""
Poner Indices
"""
df3 = pd.DataFrame (
                    arr_rand,
                    columns =['Estatura(cm)','Peso(gr)','Edad (anios)'],
                    index=['Adrian','Nika']
                   )

"""
Acceder a los datos
"""
df3['Edad (anios)']['Nika']








