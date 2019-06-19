# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:27:23 2019

@author: Galo
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado= 'C:/Users/Galo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/Data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

################## Ejercicios 1 ############################
anos_contados = df_completo_pickle['year'].value_counts()
writer = pd.ExcelWriter('formato1.xlsx', engine = 'xlsxwriter')
anos_contados.to_excel(writer, sheet_name = 'Años')
hoja_anos= writer.sheets['Años']

rango_celdas = 'B1:B{}'.format(len(anos_contados.index)+1)

formato1 ={
        'type': 'icon_set',
        'icon_style': '5_ratings',
        'icons': [{'criteria': '>=', 'type': 'number', 'value': 1000},
                  {'criteria': '>',  'type': 'number', 'value': 100},
                  {'criteria': '>',  'type': 'number', 'value': 50},
                  {'criteria': '>=',  'type': 'number', 'value': 25}]
        }


    
hoja_anos.conditional_format(rango_celdas,formato1)

writer.save()


################## Ejercicios 2 ############################
artistas_titulos = df_completo_pickle['title'].value_counts()
writer = pd.ExcelWriter('formato2.xlsx', engine = 'xlsxwriter')
artistas_titulos.to_excel(writer, sheet_name = 'Color')
hoja_color= writer.sheets['Color']

rango_celdas = 'B1:B{}'.format(len(artistas_titulos.index)+1)

formato2 ={
        'type': '3_color_scale',
        'min_color': '#C5D9F1',
        'mid_color': '#C5D8F3',
        'max_color': '#538ED5',
        }
    
hoja_color.conditional_format(rango_celdas,formato2)

writer.save()

################## Ejercicios 3 ############################
df = df_completo_pickle.iloc[49980:50800,:].copy()

artistas_nombre= df['artist'].value_counts()
writer = pd.ExcelWriter('formato3.xlsx', engine = 'xlsxwriter')
artistas_nombre.to_excel(writer, sheet_name = 'Nombre Artista')
hoja_nombre= writer.sheets['Nombre Artista']

rango_celdas = 'B1:B{}'.format(len(artistas_nombre.index)+1)

formato3 = {
        'type': 'data_bar',
        'bar_color': '#2ECC71'
        }

hoja_nombre.conditional_format(rango_celdas,formato3)

writer.save()                                       
                                        
                                        
################## Ejercicios 4 ############################                                        
df_agrupado_ano= df_completo_pickle.groupby('year') 
ano = df_agrupado_ano.size().sort_values(ascending=True) 


writer = pd.ExcelWriter('formato4.xlsx', engine = 'xlsxwriter')
ano.to_excel(writer, sheet_name = 'Año')
hoja_nombre= writer.sheets['Año']

rango_celdas = 'B1:B{}'.format(len(ano.index)+1)                               


formato4 = {
        'type': 'icon_set',
        'icon_style': '4_arrows',
        'icons': [{'criteria': '>=', 'type': 'number', 'value': 1000},
                  {'criteria': '>',  'type': 'number', 'value': 100},
                  {'criteria': '>',  'type': 'number', 'value': 50},
                  {'criteria': '>',  'type': 'number', 'value': 1}]
        }    

hoja_nombre.conditional_format(rango_celdas,formato4)

writer.save()                             
                                        
                                        