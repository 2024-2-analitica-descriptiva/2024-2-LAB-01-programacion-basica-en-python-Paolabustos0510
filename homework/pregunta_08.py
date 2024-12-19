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


def pregunta_08(datos):
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    asociacion = {}
    
    for fila in datos:
        valor_columna_2 = int(fila[1])  # Columna 2 convertida a entero
        letra_columna_1 = fila[0]      # Columna 1 (letra)
        
        if valor_columna_2 not in asociacion:
            asociacion[valor_columna_2] = set()
        
        asociacion[valor_columna_2].add(letra_columna_1)
    
    # Convertir a lista de tuplas con las letras ordenadas
    resultado = [(clave, sorted(letras)) for clave, letras in asociacion.items()]
    resultado.sort()  # Ordenar por el valor de la columna 2
    return resultado

resultado_pregunta_08 = pregunta_08(datos)
print(resultado_pregunta_08)