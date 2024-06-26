# -*- coding: utf-8 -*-
"""El arte de la analitica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NJAWPiVWwOifpTIWfyQlRRCqvhGXozw7
"""

import pandas as pd

data = pd.read_csv('avocado_full.csv')

las_vegas_data = data[data['region'] == 'LasVegas']

las_vegas_data

"""Primero se hace la región de Charlotte"""

Charlotte_data = data[data['region'] == 'Charlotte']

"""Se hace la separación para que solo se consideren los datos de esta región"""

produccion_total_Charlotte = Charlotte_data['Total Bags'].sum()
produccion_promedio_Charlotte = Charlotte_data['Total Bags'].mean()
produccion_desviacion_estandar_Charlotte = Charlotte_data['Total Bags'].std()

"""Se hace la suma total de producción en Charlotte, el promedio y la desviación estandar"""

small_bags_Charlotte = Charlotte_data['Small Bags'].sum()
large_bags_Charlotte = Charlotte_data['Large Bags'].sum()
xlarge_bags_Charlotte = Charlotte_data['XLarge Bags'].sum()

"""Se suman cada uno de los tamaños de las bolsas para sacar el porcentaje"""

porcentaje_small_Charlotte = (small_bags_Charlotte / produccion_total_Charlotte) * 100
porcentaje_large_Charlotte = (large_bags_Charlotte / produccion_total_Charlotte) * 100
porcentaje_xl_Charlotte = (xlarge_bags_Charlotte / produccion_total_Charlotte) * 100

"""Se saca el porcentaje de bolsas por tamaño"""

print("Producción total de Charlotte:", produccion_total_Charlotte)
print("Producción promedio de Charlotte:", produccion_promedio_Charlotte)
print("Desviación estándar de la producción de Charlotte:", produccion_desviacion_estandar_Charlotte)
print("Porcentaje por tamaño de bolsa chica de Charlotte:", porcentaje_small_Charlotte)
print("Porcentaje por tamaño de bolsa grande de Charlotte:", porcentaje_large_Charlotte)
print("Porcentaje por tamaño de bolsa extra grande de Charlotte:", porcentaje_xl_Charlotte)

NewYork_data = data[data['region'] == 'NewYork']

produccion_total_NewYork = NewYork_data['Total Bags'].sum()
produccion_promedio_NewYork = NewYork_data['Total Bags'].mean()
produccion_desviacion_estandar_NewYork = NewYork_data['Total Bags'].std()

small_bags_NewYork = NewYork_data['Small Bags'].sum()
large_bags_NewYork = NewYork_data['Large Bags'].sum()
xlarge_bags_NewYork = NewYork_data['XLarge Bags'].sum()

porcentaje_small_NewYork = (small_bags_NewYork / produccion_total_NewYork) * 100
porcentaje_large_NewYork = (large_bags_NewYork / produccion_total_NewYork) * 100
porcentaje_xl_NewYork = (xlarge_bags_NewYork / produccion_total_NewYork) * 100

print("Producción total de Nueva York:", produccion_total_NewYork)
print("Producción promedio de Nueva York:", produccion_promedio_NewYork)
print("Desviación estándar de la producción de Nueva York:", produccion_desviacion_estandar_NewYork)
print("Porcentaje por tamaño de bolsa chica de Nueva York:", porcentaje_small_NewYork)
print("Porcentaje por tamaño de bolsa grande de Nueva York:", porcentaje_large_NewYork)
print("Porcentaje por tamaño de bolsa extra grande de Nueva York:", porcentaje_xl_NewYork)

California_data = data[data['region'] == 'California']

produccion_total_California = California_data['Total Bags'].sum()
produccion_promedio_California = California_data['Total Bags'].mean()
produccion_desviacion_estandar_California = California_data['Total Bags'].std()

small_bags_California = California_data['Small Bags'].sum()
large_bags_California = California_data['Large Bags'].sum()
xlarge_bags_California = California_data['XLarge Bags'].sum()

porcentaje_small_California = (small_bags_California / produccion_total_California) * 100
porcentaje_large_California = (large_bags_California / produccion_total_California) * 100
porcentaje_xl_California = (xlarge_bags_California / produccion_total_California) * 100

print("Producción total de California:", produccion_total_California)
print("Producción promedio de California:", produccion_promedio_California)
print("Desviación estándar de la producción de California:", produccion_desviacion_estandar_California)
print("Porcentaje por tamaño de bolsa chica de California:", porcentaje_small_California)
print("Porcentaje por tamaño de bolsa grande de California:", porcentaje_large_California)
print("Porcentaje por tamaño de bolsa extra grande de California:", porcentaje_xl_California)

"""Se puede observar que California tiene la producción total más alta, después va Nueva York y finalmente Charlotte. Esto sugiere que California es líder en la producción de aguacates, con más información se podría decir si es por los cuidados que se les da o por el tipo de clima

Viendo la producción promedio se puede inferir que California tiene una producción total más alta que las otras dos regiones. Después sigue Nueva York y por último Charlotte.

California tiene la mayor desviación estándar, esto significa que son menos constantes al momento de su producción esto se puede dar por distintas variables. Nueva York tiene la desviación estandar menor, esto significa que tienen una menor variabilidad en comparación de las otras regiones.


En las tres regiones la mayor parte de la producción total se encuentra en bolsas pequeñas. Pero, en California, una parte significativa también se encuentra en las bolsas grandes y extra grandes.


California tiene la producción total más altas, pero también tienen una desviacipon estandar mayor.


"""