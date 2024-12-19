"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def cargar_datos(file_path):
    datos = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in file:
            # Dividir los datos por tabulación o un espacio
            datos.append(linea.strip().split('\t'))
    return datos
       
data= "../files/input/data.csv"
datos = cargar_datos(data)

def pregunta_02(datos):
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

resultado_pregunta_02 = pregunta_02(datos)
print(resultado_pregunta_02)
