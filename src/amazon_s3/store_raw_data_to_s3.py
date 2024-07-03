import logging
import json
def store_raw_data_to_s3(data):
    '''
    Modela el almacenamiento de datos crudos en un
    bucket S3
    '''
    logging.info("Guardando datos crudos en S3...") # Registra el inicio de la ejecución de la tarea

    # Verificar si la clave 'key' está presente en la data
    if 'key' not in data:
        logging.error("Clave 'key' no encontrada en los datos proporcionados.")
        return data

    #Simular la construcción de un objeto de datos crudos para S3
    raw_data = {
        "bucket": "my-raw-data-bucket", #Nombre del bucket
        "key": f"raw/{data['key']}",
        "body": json.dumps(data.get("excel_data"))
    }
    data["raw_data_s3"] = raw_data  #almacenamos el objeto en la data
    return data
