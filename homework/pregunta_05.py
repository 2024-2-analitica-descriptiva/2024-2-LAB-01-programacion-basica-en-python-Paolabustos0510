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

def pregunta_05(datos):
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

resultado_pregunta_05= pregunta_05(datos)
print(resultado_pregunta_05)