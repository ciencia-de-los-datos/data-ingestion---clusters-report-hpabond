"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data(file_path):
    # Inicializar listas para cada columna
    cluster_list = []
    cantidad_list = []
    porcentaje_list = []
    palabras_clave_list = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_cluster = None  
    palabras_clave = []  

    for line in lines:
        parts = line.split()
        
        if not parts:  
            continue

        if parts[0].isdigit():  
            if current_cluster is not None:
                cluster_list.append(current_cluster)
                palabras_clave_list.append(' '.join(palabras_clave))
            
            current_cluster = parts[0]
            cantidad_list.append(parts[1])
            porcentaje_list.append(parts[2])  
            palabras_clave = parts[4:]
        else:
            palabras_clave.extend(parts)


    if current_cluster is not None:
        cluster_list.append(current_cluster)
        palabras_clave_list.append(' '.join(palabras_clave))

    # Crear el DataFrame
    data = {
        'Cluster': cluster_list,
        'Cantidad de palabras clave': cantidad_list,
        'Porcentaje de palabras clave': porcentaje_list,
        'Principales palabras clave': palabras_clave_list
    }
    df = pd.DataFrame(data)

    # Cambiar los nombres de las columnas a minúsculas
    df.columns = map(str.lower, df.columns)

    return df