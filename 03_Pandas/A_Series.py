#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:14:37 2019

@author: VeronicaOlmedo
"""

print("Hola")

nombre= "Nika"
edad= 24

print(nombre)



import numpy as np
import pandas as pd

"""
Series
"""
lista_numeros =[1,2,3,4]
tupla_numeros =(1,2,3,4)
np_numeros = np.array ([1,2,3,4])

numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "Adrian",
        (),
        [],
        {"nombre":"Nika"}
        ])

numero_series_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]

series_ciudades = pd.Series(lista_ciudades,
                            index=["4","5","1","17"])


series_ciudades["17"]

series_ciudades[0]
series_ciudades[1]
series_ciudades[2]
series_ciudades[3]

print(type(series_ciudades))

"""
Diccionario
"""
valores_ciudad = {
        "Ibarra" : 9500,
        "Guayaquil": 10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]


ciudades_menor_5000=serie_valor_ciudad < 5000
ciudades_menor_5000=serie_valor_ciudad == 5000
ciudades_menor_3300=serie_valor_ciudad == 3300

serie_menor_5000 = serie_valor_ciudad[ciudades_menor_5000] // Condicionales

serie_valor_ciudad = serie_valor_ciudad * 1.1 // Operaciones

serie_valor_ciudad["Quito"] = 3300


print("Lima" in serie_valor_ciudad) #False
print("Loja" in serie_valor_ciudad) #True

np.square(serie_valor_ciudad)

np.sin(serie_valor_ciudad)


ciudades_uno = pd.Series({
        "Quito": 1500,
        "Loja":4000,
        "Cuenca":2000
        })



ciudades_dos = pd.Series({
        "Montañita": 300,
        "Guayaquil":1000,
        "Quito":2000
        })

print(ciudades_uno * ciudades_dos) # Solo multiplica los indices que estan en los dos listas

randomico = np.random.rand(3)# Numeros Aleatorios

serie_tres_rand = pd.Series(randomico)

#Arreglo de indices
ciudades_uno.index

serie_uno = pd.Series({
        "Madrid":4000,
        "Barcelona":5000
        })

serie_dos = pd.Series({
        "Zaragoza":1000,
        "Cuenca":3000
        })

#CONCATENAR SERIES
serie_add = serie_uno.add(serie_dos)

serie_concatenar = pd.concat([serie_uno,serie_dos])

serie_concatenar_v = pd.concat([serie_uno,serie_dos], verify_integrity=True) #Sale como error todos los que se repiten

serie_append = serie_uno.append(serie_dos)

# AÑADIR UN NUEVO ITEM

serie_uno_uno= pd.Series({"Valencia":5000})

serie_anadir = serie_uno.append(serie_uno_uno)

#MAX

serie_uno.max()

pd.Series.max(serie_uno)

np.max(serie_uno)

#MIN
serie_uno.min()

pd.Series.min(serie_uno)

np.min(serie_uno)


#ESTADISTICA AVG MEAN
serie_uno.mean()

pd.Series.median(serie_uno)

np.average(serie_uno)

#Primer (5)
serie_uno.head(2)

#Ultimo
serie_uno.tail(2)


serie_uno.sort_values().head(2)
serie_uno.sort_values().tail(2)

serie_uno.sort_values(ascending = False).head(2)
serie_uno.sort_values(ascending = False).head(2)

# 0     >= 1000      5%
# 1000  >= 10000    10%
# 10000 >           15%

def calculo (valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor >1000 and valor <= 10000):
        return valor * 1.15
    if(valor > 10000):
        return valor * 1.15


serie_uno.map(calculo)
serie_uno.apply(calculo)

serie_uno.where(serie_uno > 1000,serie_uno * 1.05)


















































