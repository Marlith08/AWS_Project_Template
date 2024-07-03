import logging
# Recibir mensajes de la cola
def receive_messages_from_queue(data):
    '''
    Simula la recepción de mensajes desde una cola SQS y
    guarda el mensaje recibido en la data.
    '''
    try:
        # Registra el inicio de la ejecución de la tarea
        logging.info("Recibiendo mensajes de la cola...")
        # Simulación de recepción de mensaje desde SQS
        message_id = "msg-123"
        message_body = "This is a message from SQS"

        #Guardar el mensaje recibido en los datos
        message = {
            "message_id": message_id,
            "body": message_body
        }
        data["sqs_message"] = message
    except Exception as e:
        # Registra un mensaje de error en caso de excepción
        logging.error(f"Error al recibir mensajes de la cola: {str(e)}")

    return data #Retorna la data actualizada