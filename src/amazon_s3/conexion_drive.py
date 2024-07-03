# Código realizado en base a canales de youtube, github y soporte de errores con chatgpt
# https://github.com/cesardramirez/python-rest-google-drive.git
# https://www.youtube.com/watch?v=rIPp7Yg8s6g
# https://github.com/aluna1997/Python_and_PyDrive2.git
# https://www.youtube.com/watch?v=ZI4XjwbpEwU

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

#Ruta a tu archivo JSON de credenciales de Drive
SERVICE_ACCOUNT_FILE = 'C:\\Users\\anton\\Documents\\CDR\\src\\amazon_s3\\almacenamiento-428217-1a170f7cc8a9.json'

def get_drive_service():
    '''
    Autenticación y obtención del servicio Google Drive
    '''
    scopes = ['https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=scopes)
    service = build('drive', 'v3', credentials=credentials)
    return service

def upload_file_to_drive(file_path, drive_folder_id):
    '''
    Modela la carga de un archivo a Google Drive
    '''

    service = get_drive_service()
    file_name = os.path.basename(file_path)
    file_metadata = {
        'name': file_name,
        'parents': [drive_folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File {file_name} uploaded to Google Drive with ID: {file.get('id')}")


def download_file_from_drive(file_id, destination_path):
    '''
    Modela la descarga archivo desde Google Drive
    '''
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    with open(destination_path, 'wb') as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")