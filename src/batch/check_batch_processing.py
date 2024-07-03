import logging
def check_batch_processing(data):
    '''
    Simula el procesamiento por lotes y añade
    la información a la data
    '''
    logging.info("Procesamiento por lotes...")  # Registra el inicio de la ejecución de la tarea

    #Simulación de datos de procesamiento por lotes
    batch_data = {
        "job_id": "batch-123",  #ID del trabajo
        "status": "completed"   #estado del trabajo
    }
    data["batch_processed"] = batch_data    #Alamacenar el procesamiento por lotes a la data
    return data #Retorna la data actualizada