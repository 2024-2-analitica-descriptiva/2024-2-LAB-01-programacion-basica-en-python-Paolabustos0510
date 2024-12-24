"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
data = os.path.join(os.path.dirname(__file__), "../files/input/data.csv")
datos = []
with open( data, 'r', encoding='utf-8') as file:
    for linea in file:
        datos.append(linea.strip().split('\t'))
 

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    dic_clave_columna_1 = {}
    for fila in datos:
        letra = fila[0]
        valores_columna_5 = fila[4].split(",")
        for x in valores_columna_5:
            valor = int(x.split(":")[1])
          

            if letra in dic_clave_columna_1:
                dic_clave_columna_1[letra]+= valor
            else:
                dic_clave_columna_1[letra] = valor

    return dict(sorted(dic_clave_columna_1.items()))

