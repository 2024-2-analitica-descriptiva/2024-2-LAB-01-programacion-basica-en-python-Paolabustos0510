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
 

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    dic_suma = {}
    for fila in datos:
        valor_columna_2 = int(fila[1])
        valor_columna_4 = fila[3].split(",")
        for letra in valor_columna_4:
            if letra in dic_suma:
                dic_suma[letra]+= valor_columna_2
            else:
                dic_suma[letra] = valor_columna_2
    return dict(sorted(dic_suma.items()))
    
