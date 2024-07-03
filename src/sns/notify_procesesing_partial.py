import logging
from src.sns.send_email import send_email, send_notification_and_email
def notify_procesesing_partial(data):

    '''
    Simula al servicio SNS enviando una notificación con un
    contenido personalizado
    '''

    # Registra el inicio de la ejecución de la tarea
    logging.info("Enviando notificación de procesamiento parcial de sus archivos...")

    data["sns_notification"] = "Notificación de Procesamiento Parcial de sus archivos"

    #Configuración del correo
    subject = "Notificación de Procesamiento Parcial de sus archivos"
    body = "El procesamiento parcial de datos ha sido completado exitosamente."
    recipient = "antony.mendoza@upch.pe"  #Correo del destinatario

    #Envio del correo
    send_email(subject, body, recipient)
    send_notification_and_email(subject, body, recipient)

    return data #Retorna la data actualizada