"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    
    file_path = 'clusters_report.txt'
    

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
        'cluster': cluster_list,
        'cantidad_de_palabras_clave': cantidad_list,
        'porcentaje_de_palabras_clave': porcentaje_list,
        'principales_palabras_clave': palabras_clave_list
    }
    df = pd.DataFrame(data)

    # Cambiar los nombres de las columnas a minúsculas
    df.columns = map(str.lower, df.columns)

# Convertir las columnas a enteros
    df['cluster'] = df['cluster'].astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.').astype(float)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].astype(str)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('.')

    return df

