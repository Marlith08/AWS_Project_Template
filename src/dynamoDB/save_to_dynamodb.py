import logging
import pandas as pd
from src.amazon_s3.conexion_drive import upload_file_to_drive

def save_to_dynamodb(data):
    '''
    Almacenamiento de los datos procesados en un archivo Excel
    de manera local y cargarlo a Google Drive
    '''

    logging.info("Guardando datos en DynamoDB...")  # Registra el inicio de la ejecución de la tarea

    processed_data = data.get("processed_data", []) #Obtiene los datos procesados del diccionario de datos

    #Guardar un archivo Excel de manera local
    df = pd.DataFrame(processed_data)
    excel_filename = "processed_data.xlsx"
    df.to_excel(excel_filename, index=False)
    logging.info(f"Datos procesados guardados en: {excel_filename}")    # Registra el inicio de la ejecución de la tarea

    #Subir el archivo Excel a Google Drive
    upload_file_to_drive(excel_filename, '1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V')

    return data #Retorna un diccionario con la data, pero sin muchos cambios