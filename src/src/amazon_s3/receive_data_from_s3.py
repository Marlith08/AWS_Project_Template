#La parte de código para enviar el correo también nos vasamos de las fuentes
#presentadas en el archivo conexion_drive.py

import logging
import pandas as pd
from src.sns.send_email import send_email, send_notification_and_email
from src.amazon_s3.conexion_drive import download_file_from_drive

def receive_data_from_s3(data):
    '''
     Simula el proceso de recibir datos desde S3, incluyendo la descarga de un archivo Excel desde
    Google Drive, lectura del archivo Excel y envío de notificaciones por correo electrónico.
    '''
    logging.info("Recibiendo datos desde S3 (simulación de Excel)...") # Registra el inicio de la ejecución de la tarea

    #Descargar un archivo desde Google Drive
    download_file_from_drive('1KVDnByJB-7Hi1G3syDfDy1lHvKlGlNj1', 'file.xlsx')

    #Simulamos la lectura de un archivo Excel
    excel_file = pd.ExcelFile('file.xlsx')
    sheet_name = excel_file.sheet_names[0]  # Supongamos que tomamos la primera hoja
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Convertir los datos del DataFrame a un formato adecuado
    excel_data = df.to_dict(orient='records')
    data["excel_data"] = excel_data

    logging.info("Enviando notificación de carga de archivos...")   # Registra el inicio de la ejecución de la tarea

    #Redacción del correo
    subject = "Notificación de carga de archivos"
    body = "El archivo se ha cargado correctamente."
    recipient = "antony.mendoza@upch.pe"  #Correo del destinatario

    send_email(subject, body, recipient) # Enviar correo electrónico de notificación
    send_notification_and_email(subject, body, recipient)   #Enviar notificación y correo electrónico simultáneamente

    return data