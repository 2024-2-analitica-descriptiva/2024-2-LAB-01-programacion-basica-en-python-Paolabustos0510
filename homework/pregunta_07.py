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
 

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    asociacion = {}
    
    for fila in datos:
        valor_columna_2 = int(fila[1])  # Columna 2 convertida a entero
        letra_columna_1 = fila[0]      # Columna 1 (letra)
        
        if valor_columna_2 not in asociacion:
            asociacion[valor_columna_2] = []
        
        asociacion[valor_columna_2].append(letra_columna_1)
    
    # Convertir a lista de tuplas y ordenar por el valor de la columna 2
    resultado = sorted((clave, letras) for clave, letras in asociacion.items())
    return resultado

