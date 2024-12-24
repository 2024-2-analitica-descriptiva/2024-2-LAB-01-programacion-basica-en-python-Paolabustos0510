"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

data = r"files\input\data.csv"
datos = []
with open( data, 'r', encoding='utf-8') as file:
    for linea in file:
        datos.append(linea.strip().split('\t'))
 

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    
    for fila in datos:
        # Obtener la columna 5 y dividirla por comas
        elementos = fila[4].split(",")
        for elemento in elementos:
            clave, valor = elemento.split(":")  # Separar clave y valor
            valor = int(valor)  # Convertir el valor a entero
            
            if clave in valores_por_clave:
                # Actualizar máximo y mínimo
                valores_por_clave[clave]['max'] = max(valores_por_clave[clave]['max'], valor)
                valores_por_clave[clave]['min'] = min(valores_por_clave[clave]['min'], valor)
            else:
                # Inicializar máximo y mínimo
                valores_por_clave[clave] = {'max': valor, 'min': valor}
    
    # Convertir a lista de tuplas (clave, minimo, maximo) y ordenar alfabéticamente por clave
    resultado = sorted((clave, valores['min'], valores['max']) for clave, valores in valores_por_clave.items())
    return resultado

