#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:10 2019

@author: VeronicaOlmedo
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

# Tres Archivos para exportar los datos
# Json
# SQL
# Excel

# Crear un df mas pequeño para que no se demore

df = df_completo_pickle.iloc[49980:50019,:].copy()

#############EXCEL#####################3

df.to_excel('ejemplo_basico.xlsx')

#Quitar los indices

df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

#Trear columnas especificas 
columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)


# Multiples hojas de trabajo (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')
df.to_excel(writer, sheet_name = 'Preview Dos', index = False)
df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()


# Formateo Condicional

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

#Cuantos artistas existen 
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1) #Para que se escogan todas las filas

formato = {
        'type': '2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'min_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()


######################### SQL ##################################

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('Tabla', conexion)
    
## with mysql.connect('mysql://user:password@ip:puerto/bd') as conexion
##    df.to_sql('Tabla', conexion)

######################### JSON #################################

df.to_json('artist.json')

df.to_json('artist_ordientados_tabla.json', orient='table')



################## Ejercicios ############################
artistas_contados = df_completo_pickle['artist'].value_counts()
writer = pd.ExcelWriter('formato1.xlsx', engine = 'xlsxwriter')
artistas_contados.to_excel(writer, sheet_name = 'Criterio')
hoja_criterio= writer.sheets['Criterio']

hoja_criterio = 'A1:D1{}'.format(len(artistas_contados.index)+1),

formato1 ={
        'type': 'icon_set',
        'icon_style': '4_red_to_black',
        'icons': [{'criteria': '>=', 'type': 'number',     'value': 90},
                  {'criteria': '<',  'type': 'percentile', 'value': 50},
                  {'criteria': '<=', 'type': 'percent',    'value': 25}]
        }


    
hoja_artistas.conditional_format(rango_celdas,formato1)

writer.save()



artistas_contados = df_completo_pickle['artist'].value_counts()
writer = pd.ExcelWriter('formato2.xlsx', engine = 'xlsxwriter')
artistas_contados.to_excel(writer, sheet_name = 'Color')
hoja_color= writer.sheets['Color']

rango_celdadas = 'F3:F14{}'.format(len(artistas_contados.index)+1),

formato2 ={
        'type': 'data_bar',
        'bar_color': '#63C384'
        }
    
hoja_color.conditional_format(rango_celdas,formato2)

writer.save()




















