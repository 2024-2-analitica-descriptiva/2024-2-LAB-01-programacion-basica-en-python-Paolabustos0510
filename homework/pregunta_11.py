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

def pregunta_11(datos):
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
    
resultado_pregunta_11 = pregunta_11(datos)
print(resultado_pregunta_11)