"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def cargar_datos(file_path):
    """
    Carga un archivo de texto estructurado como el compartido.
    :param file_path: Ruta del archivo de datos.
    :return: Lista de listas donde cada sublista representa una fila.
    """
    datos = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in file:
            # Dividir los datos por tabulación o un espacio
            datos.append(linea.strip().split('\t'))
    return datos

data= "../files/input/data.csv"
datos = cargar_datos(data)

def pregunta_10(datos):
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    lista_tuplas = []
    
    for fila in datos:
        letra = fila[0]  # Primera columna 
        valor_1 = (fila[3].split(","))
        cantidad_columna_4 = len(valor_1)
        valor_2 = (fila[4].split(","))
        cantidad_columna_5 = len(valor_2)
        lista_tuplas.append((letra, cantidad_columna_4, cantidad_columna_5))
        
    return lista_tuplas
  
resultado_pregunta_10 = pregunta_10(datos)
print(resultado_pregunta_10)