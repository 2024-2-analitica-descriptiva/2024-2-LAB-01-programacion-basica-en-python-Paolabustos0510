"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
data = r"files\input\data.csv"
datos = []
with open( data, 'r', encoding='utf-8') as file:
    for linea in file:
        datos.append(linea.strip().split('\t'))
 

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_columna = {}
    
    for fila in datos:
        letra = fila[0]  
        valor = int(fila[1])  
        
        if letra in suma_columna:
            suma_columna[letra] += valor
        else:
            suma_columna[letra] = valor
    
        resultado_suma_columna = sorted(suma_columna.items())
    return resultado_suma_columna

