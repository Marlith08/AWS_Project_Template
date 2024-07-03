import logging
import json
import pandas as pd
from src.amazon_s3.conexion_drive import upload_file_to_drive

def save_advanced_results_to_s3(data):
    '''
    Guarda los resultados procesados hasta este punto en Google Drive
    y se hace una copia local en formato excel y json
    '''
    logging.info("Guardando resultados avanzados en S3...")
    advanced_results = data.get("advanced_results", [])

    # Guardar resultados en un archivo JSON en Google Drive
    json_data = json.dumps(advanced_results)
    with open('advanced_results.json', 'w') as file:
        file.write(json_data)

    # Guardar en archivo Excel localmente
    df = pd.DataFrame(advanced_results)
    excel_filename = "advanced_results.xlsx"
    df.to_excel(excel_filename, index=False)

    # Subir archivo JSON a Google Drive
    upload_file_to_drive('advanced_results.xlsx',
                         '1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V')
    upload_file_to_drive('advanced_results.json', '1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V')

    logging.info(f"Resultados avanzados guardados en: {excel_filename}")    # Registra el inicio de la ejecución de la tarea

    return data #Retorna la data actualizada