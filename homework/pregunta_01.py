"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os
data = os.path.join(os.path.dirname(__file__), "../files/input/data.csv")
datos = []
with open(data, 'r', encoding='utf-8') as file:
    for linea in file:
        datos.append(linea.strip().split('\t'))
 
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    for fila in datos:
        suma += int(fila[1])  
    return suma    

