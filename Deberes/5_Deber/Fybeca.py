# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:34:33 2019

@author: VeronicaOlmedo
"""

import numpy as np
import pandas as pd
import re

# productos = response.xpath('/html/body/div/div/div/div/div/ul/li/@data-name').extract()
# productos = response.xpath('//a[contains(@class, "name")]/text()').extract()
productos = ['SHAMPOO JOHN FRIEDA BRILLANT BRUNETTE VISIBLY DEEPER, OSCURECE EL COLOR (DEPOSITO SEMIPERMANENTE)',
 'SHAMPOO JOHN FRIEDA BEYND SMOTH FRZ IMMUNITY',
 'SHAMPOO BRILLANT BRUNETTE VISIBLY BRIGHTER,ACLARA EL COLOR (ELEVADO PERMANENTE)',
 'SHAMPOO JOHN FRIEDA  FRZ ESE MIRACULOUS RECOVE',
 'BB+ ACONDICIONADOR BEAUTIK SIN ENJUAGUE OLIO DI ARGAN 200 ML',
 'SHAMPOO TRICOVIT WNT FRASCO 150 ML',
 'SHAMPOO ANTICASPA HEAD & SHOUL PROTECCION CAIDA 180 ML',
 'SHAMPOO COCONUT CURLS 385ML',
 'MASCARILLA HENNA PLATINADOS MATIZANTE DE CANAS 225 ML',
 'SHAMPOO HEAD & SHOULDERS NUTRICION PROFUNDA 180 ML',
 'SHAMPOO HEAD & SHOULDERS NUTRICION PROFUNDA 375 ML',
 'SHAMPOO HEAD & SHOULDERS NUTRICION PROFUNDA 700 ML',
 'SHAMPOO KATIVA CABELLO FINO VOLUME+  250ML',
 'SHAMPOO CABELLO KLORANE SHAMPOO PAPYRUS',
 'JOLLY SHAMPOO FAMILIAR CABELLOS GRASOS 850ML',
 'SHAMPOO SYOSS CERAMIDAS 500ML',
 'SHAMPOO SEDAL BY YUYA TE VERDE Y LIMON PUREZA DETOX 650ML',
 'SHAMPOO SEDAL BY YUYA TE VERDE Y LIMON PUREZA DETOX  340ML',
 'PACK SHAMPOO + ACONDICIONADOR DOVE RECONSTRUCCION COMPLETA 400ML',
 'EDAPIL CHAMPU 120ML',
 'SHAMPOO ORGANIX ARGAN OIL OF MOROCCO',
 'PACK PANTENE SHAMPO SUMMER 400 ML+CREMA DE PEINAR 300ML 50% DESCUENTO',
 'SYOSS SH ANTICASPA X 500 ML',
 'ELVIVE OLEO EXTRAORD. RIZOS DEFINIDOS SH 750 ML',
 'SHAMPOO ANTICASPA FYBECA HIDRATC/SUAVIDAD 400 ML']

# response.xpath('//div[contains(@class,"product-list")]/div[@data-name]').extract()
precio = ['<div data-bind="text:\'$\' + (12.64).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.64).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.64).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.64).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.12).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (25.20).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (4.57).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.00).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.51).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (4.79).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (8.20).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.99).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (5.75).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (14.79).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.13).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.85).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (4.96).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (3.45).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.86).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (16.08).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (12.00).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (10.32).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.28).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (11.86).formatMoney(2, \'.\', \',\')"></div>',
 '<div data-bind="text:\'$\' + (6.07).formatMoney(2, \'.\', \',\')"></div>']

#Obtencion de los precios con expreciones regulares
for i in range(len(precio)):
    precio[i] = re.findall(r"\d\d.\d.|\d.\d.", precio[i])
    print(precio)


df_completo = pd.DataFrame(precio,columns=['Precio'],
                          index=productos) 

#Cambiar el dataframe en la columna de precios se un str a float
df_completo['Precio'] = pd.to_numeric(df_completo['Precio'])

#Saca el maximo valor 
df_maximo= df_completo.values.max()
print(df_completo.loc[df_completo['Precio'] == df_completo['Precio'].max()])

#Saca el valor minimo del df
df_minimo= df_completo.values.min()

print(df_completo.loc[df_completo['Precio'] == df_completo['Precio'].min()])

