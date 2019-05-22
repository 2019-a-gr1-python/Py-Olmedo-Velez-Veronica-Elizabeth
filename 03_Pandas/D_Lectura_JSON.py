#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:51 2019

@author: VeronicaOlmedo
"""

import json
import pandas as pd
import os

path= '/Users/VeronicaOlmedo/Documents/GitHub/Py-Olmedo-Velez-Veronica-Elizabeth/03_Pandas/artwork'

archivo = '/a/000/a00001-1035.json'

path_archivo = path + archivo

#Llaves que necesitamos 
llaves = ['id','all_artists',
          'title','medium',
          'dateText','acquisitionYear',
          'height','width','units']

#registro = [[1,2,3,4,4,5,56,7,8,8,9,9,0]] #Guardar todos los datos con las llaves en la lista

#Cierra automaticamente el archivo despues de abrirlo 

with open(path_archivo) as texto_json:
    contenido_json = json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
    registro_df_lista=[]
    for llave in llaves:
        valor = contenido_json[llave]#acceder al json
        registro_df_lista.append(valor)
        
    registro_df_tupla= tuple(registro_df_lista) #Guardar en una tupla el registro

print (registro_df_tupla)
df_chiquito = pd.DataFrame([registro_df])
df_chiquito_t = pd.DataFrame([registro_df_tupla])
#Muestra un diccionario de datos

#Funciones con JSON
def leer_json(path,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
        registro_df_lista=[]
        for llave in llaves:
            valor = contenido_json[llave]#acceder al json
            registro_df_lista.append(valor)
            
        return registro_df_tupla #Guardar en una tupla el registro

leer_json(path_archivo, llaves)
















