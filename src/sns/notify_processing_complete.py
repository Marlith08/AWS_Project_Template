import logging
from src.sns.send_email import send_email, send_notification_and_email
def notify_processing_complete(data):
    '''
    Simula al servicio SNS enviando una notificación con un
    contenido personalizado
    '''

    # Registra el inicio de la ejecución de la tarea
    logging.info("Enviando notificación de procesamiento completo de sus archivos...")
    data["sns_notification"] = "Notificación de Procesamiento Completo"

    #Configuración del correo
    subject = "Notificación de Procesamiento Completo"
    body = "El procesamiento de datos ha sido completado exitosamente."
    recipient = "antony.mendoza@upch.pe"  #Correo del destinatario

    #Envio del correo
    send_email(subject, body, recipient)
    send_notification_and_email(subject, body, recipient)

    return data #Retorna la data actualizada