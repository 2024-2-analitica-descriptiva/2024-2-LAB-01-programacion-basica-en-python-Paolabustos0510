"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

data= r"C:\Users\Olga\Documents\GitHub\2024-2-LAB-01-programacion-basica-en-python-Paolabustos0510\files\input\data.csv"

datos = []
with open( data, 'r', encoding='utf-8') as file:
    for linea in file:
        datos.append(linea.strip().split('\t'))               

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {} 
    for fila in datos:
        letra = fila[0] 
        if letra in conteo:
            conteo[letra] += 1 
        else:
            conteo[letra] = 1

    resultado = sorted(conteo.items()) #sorted genera una lista ordenada, no entiendo qué hace items
    return resultado

