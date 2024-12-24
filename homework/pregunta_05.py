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
 
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    
    for fila in datos:
        letra = fila[0]  # Primera columna 
        valor = int(fila[1])  # Convertir a entero la segunda columna
        
        if letra in valores_por_letra:
            # Actualizar máximo y mínimo
            valores_por_letra[letra]['max'] = max(valores_por_letra[letra]['max'], valor) 
            valores_por_letra[letra]['min'] = min(valores_por_letra[letra]['min'], valor)
        else:
            # Inicializar máximo y mínimo
            valores_por_letra[letra] = {'max': valor, 'min': valor}
    
    # Convertir a lista de tuplas (letra, maximo, minimo) y ordenar alfabéticamente por letra
    resultado = sorted((letra, valores['max'], valores['min']) for letra, valores in valores_por_letra.items())
    return resultado

