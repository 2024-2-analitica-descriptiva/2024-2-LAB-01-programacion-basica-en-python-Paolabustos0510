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

def pregunta_12(datos):
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    dic_clave_columna_1 = {}
    for fila in datos:
        letra = fila[0]
        valores_columna_5 = fila[4].split(",")
        for x in valores_columna_5:
            valor = int(x.split(":")[1])
          

            if letra in dic_clave_columna_1:
                dic_clave_columna_1[letra]+= valor
            else:
                dic_clave_columna_1[letra] = valor

    return dict(sorted(dic_clave_columna_1.items()))

resultado_pregunta_12 = pregunta_12(datos)
print(resultado_pregunta_12)