# Código realizado en base a canales de youtube, github y soporte de errores con chatgpt
# https://github.com/joedicastro/joedicastro.com/blob/master/site/source/blog/Enviar%20un%20correo%20electr%C3%B3nico%20con%20Python.md
# https://youtu.be/oPAo8Hh8bj0?si=iYRFvmGd5a2Vm8CD
# https://gist.github.com/2624789/082fe60dd643cc624e74

import logging
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Registra el inicio de la ejecución de la tarea
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar variables de entorno desde el archivo .env
load_dotenv()
def send_email(subject, body, recipient):
    """
    Función para enviar un correo electrónico utilizando configuraciones
    de SMTP cargadas desde variables de entorno.
    """
    email_sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))  # Puerto predeterminado es 587 para TLS

    # Crear el mensaje de correo electrónico
    email_message = EmailMessage()
    email_message["From"] = email_sender
    email_message["To"] = recipient
    email_message["Subject"] = subject
    email_message.set_content(body)

    # Establecer conexión SMTP y enviar correo electrónico
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()  # Iniciar conexión con STARTTLS
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, recipient, email_message.as_string())
        logging.info(f"Correo electrónico enviado a {recipient}")
        return True
    except Exception as e:
        logging.error(f"Error al enviar correo electrónico: {str(e)}")
        return False

def send_notification_and_email(subject, body, recipient):
    """
    Función para enviar una notificación y un correo electrónico
    utilizando la función send_email.
    """
    logging.info(f"Enviando notificación y correo electrónico a {recipient}...")

    # Envío del correo electrónico
    success = send_email(subject, body, recipient)
    if success:
        # Registra el inicio de la ejecución de la tarea
        logging.info("Notificación y correo electrónico enviados correctamente.")
        return True
    else:
        # Registra el inicio de la ejecución de la tarea
        logging.error("Error al enviar notificación y correo electrónico.")
        return False