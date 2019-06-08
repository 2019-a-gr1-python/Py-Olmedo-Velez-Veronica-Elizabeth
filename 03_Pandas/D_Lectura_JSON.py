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
def leer_json(path_archivo,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leer_json(path_archivo, llaves)


#Leer todos los path nos importan archivos solo .json

def leer_json_en_carpetas(directorio,llaves):
    trabajos_arte =[]
    print(type(os.walk(directorio)))
    for path_raiz, lista_directorios, archivos in os.walk(directorio): 
        print(path_raiz)
        print(type(path_raiz))                                                  # String -> Path Actual del archivo
        print(lista_directorios)
        print(type(lista_directorios))                                          # Lista String directorios
        print(archivos)
        print(type(archivos))                                                   # Lista Strings nombre archivo
        
        for nombre_archivo in archivos:
            if nombre_archivo.endswith('json'):                                 # Te revisa la terminación de archivo necesitamos concatenar todo el path
                # logica
                directorio_archivo = os.path.join(
                        path_raiz,
                        nombre_archivo
                        )
                pieza_arte = leer_json(directorio_archivo, llaves)
                trabajos_arte.append(pieza_arte)
            
     
    df = pd.DataFrame.from_records(                                             #Debe estar identado el codigo con el primer for
              trabajos_arte,
              columns= llaves,
              index = 'id'
              )
    return df
    
df_artworks = leer_json_en_carpetas(path,llaves)














