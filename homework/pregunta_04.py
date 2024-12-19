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

def pregunta_04(datos):
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    registro_mes = {}

    for fila in datos:
        fecha = fila[2]
        mes = fecha.split("-")[1]  
        if mes in registro_mes:
            registro_mes[mes] += 1
        else:
            registro_mes[mes] = 1
    
    # Convertir a lista de tuplas y ordenar por mes
    resultado = sorted(registro_mes.items())
    return resultado
resultado_pregunta_04 = pregunta_04(datos)
print(resultado_pregunta_04)