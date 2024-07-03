import logging
def process_data_with_lambda(data):

    '''
    Simula el procesamiento de datos con Lambda
    '''
    logging.info("Procesando datos con Lambda...")  # Registra el inicio de la ejecución de la tarea
    excel_data = data.get("excel_data", []) #Obtención de los datos procesados

    processed_data = []  # Lista para almacenar los resultados

    #Iteración sobre los datos
    for item in excel_data:

        #Simulación de un procesamiento avanzado sobre cada elemento
        processed_item = {
            "ID": item["ID"],
            "ProcessedValue": item["Value"] * 2  # Ejemplo de procesamiento
        }
        processed_data.append(processed_item)   #Almacenar el calculo a la lista

    data["processed_data"] = processed_data #Almacenar los resultados en la data
    return data #Retorna la data actualizada