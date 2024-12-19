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

def pregunta_03(datos):
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

resultado_pregunta_03 = pregunta_03(datos)
print(resultado_pregunta_03)