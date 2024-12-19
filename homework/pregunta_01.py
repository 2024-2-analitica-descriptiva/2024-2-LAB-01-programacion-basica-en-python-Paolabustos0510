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
            
            datos.append(linea.strip().split('\t'))
    return datos
       
data= "../files/input/data.csv"
datos = cargar_datos(data)

def pregunta_01(datos):
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    for fila in datos:
        suma += int(fila[1])  
    return suma    
    
resultado_pregunta_01 = pregunta_01(datos)
#print(datos)
print(f'resultados: {resultado_pregunta_01}')


