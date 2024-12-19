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

def pregunta_09(datos):
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    clave_columna_5 = {}
    
    for fila in datos:
    
        elementos = fila[4].split(",")
        for elemento in elementos:
            clave, valor = elemento.split(":")  
            valor = int(valor)  
            
            if clave in clave_columna_5:
              clave_columna_5[clave] += 1
             
            else:
              clave_columna_5[clave] = 1

    resultado = dict(sorted(clave_columna_5.items()))   
    return  resultado

resultado_pregunta_09 = pregunta_09(datos)
print(resultado_pregunta_09)
