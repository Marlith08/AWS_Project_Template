import logging
import time
import json
import pandas as pd
from src.amazon_s3.conexion_drive import upload_file_to_drive
from src.step_functions.state.choice_state import ChoiceState
from src.step_functions.stateMachine import StateMachine
from src.step_functions.state.parallel_state import ParallelState
from src.step_functions.state.task_state import TaskState
from src.amazon_s3.receive_data_from_s3 import receive_data_from_s3
from src.amazon_s3.store_raw_data_to_s3 import store_raw_data_to_s3
from src.batch.check_batch_processing import check_batch_processing
from src.dynamoDB.save_to_dynamodb import save_to_dynamodb
from src.lambda_p.advanced_processing import advanced_processing
from src.lambda_p.process_data_with_lambda import process_data_with_lambda
from src.sns.notify_processing_complete import notify_processing_complete
from src.sns.notify_procesesing_partial import notify_procesesing_partial
from src.sqs.receive_messages_from_queue import receive_messages_from_queue
from src.amazon_s3.conexion_drive import get_drive_service

class RetryableTaskState(TaskState):
    '''
    Inicializa un estado de una tarea con un límite de reintentos al tener algún
    error con un tiempo de espera en segundos
    '''
    def __init__(self, name, task, next_state, retries=5, delay=1):
        super().__init__(name, task, next_state)
        self.retries = retries
        self.delay = delay

    def execute(self, data):
        attempt = 0
        # Ejecutar la tarea en caso de error
        # No se reintenta más del límite
        while attempt < self.retries:
            try:
                logging.info(f"Ejecutando tarea: {self.name}")
                data = self.task(data)
                return self.next_state, data # retorna el siguiente estado y los datos actualizados
            except Exception as e:
                attempt += 1
                logging.error(f"Error en tarea {self.name}: {str(e)}. Reintento {attempt}/{self.retries}")
                time.sleep(self.delay)

        # Se levanta una excepción después de todos los reintentos fallidos
        raise Exception(f"Tarea {self.name} falló después de {self.retries} reintentos.")

def save_advanced_results_to_s3(data):
    logging.info("Guardando resultados avanzados en S3...")
    advanced_results = data.get("advanced_results", [])

    # Guardar resultados en un archivo JSON en Google Drive
    json_data = json.dumps(advanced_results)
    with open('advanced_results.json', 'w') as file:
        file.write(json_data)

    # Subir archivos nuevos a Google Drive
    upload_file_to_drive('advanced_results.xlsx', '1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V')  # Subir archivo Excel a Google Drive
    upload_file_to_drive('advanced_results.json', '1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V')  # Subir archivo JSON a Google Drive

    # Guardar en archivo Excel localmente
    df = pd.DataFrame(advanced_results)
    excel_filename = "advanced_results.xlsx"
    df.to_excel(excel_filename, index=False)
    logging.info(f"Resultados avanzados guardados en: {excel_filename}")

    # Eliminar archivos antiguos, mantener los últimos dos archivos subidos
    service = get_drive_service()
    files = service.files().list(q=f"'{'1LWJTNqb-ZjEL_v9-SIVSoYE3J_cKXT9V'}' in parents and trashed=false", pageSize=10, fields="files(id, name, modifiedTime)", orderBy="modifiedTime desc").execute().get('files', [])
    files_to_keep = ['file.xlsx']
    for file in files:
        if file['name'] not in files_to_keep:
            service.files().delete(fileId=file['id']).execute()
            logging.info(f"Archivo antiguo eliminado: {file['name']}")

    return data

if __name__ == "__main__":
    # Configuración básica de logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Definir estados y sus tareas con reintentos
    states = {
        # Crear instancias de RetryableTaskState para tareas que requieren reintentos
        "ReceiveDataFromS3": RetryableTaskState("ReceiveDataFromS3", receive_data_from_s3, "ParallelProcessing"),
        "ParallelProcessing": ParallelState("ParallelProcessing", {
            "ProcessDataWithLambda": process_data_with_lambda,
            "SaveToDynamoDB": save_to_dynamodb,
            "notify_procesesing_partial": notify_procesesing_partial,
            "StoreRawDataToS3": store_raw_data_to_s3
        }, "ChoosePath"),
        "ChoosePath": ChoiceState("ChoosePath", [
            ("processingRequired", True, "InvokeLambdaForAdvancedProcessing"),
            ("processingRequired", False, "CheckBatchProcessing")
        ], "CheckBatchProcessing"),
        "InvokeLambdaForAdvancedProcessing": RetryableTaskState("InvokeLambdaForAdvancedProcessing", advanced_processing, "SaveAdvancedResultsToS3"),
        "SaveAdvancedResultsToS3": RetryableTaskState("SaveAdvancedResultsToS3", save_advanced_results_to_s3, "NotifyAdvancedProcessingComplete"),
        "NotifyAdvancedProcessingComplete": TaskState("NotifyAdvancedProcessingComplete", notify_processing_complete, "CheckBatchProcessing"),
        "CheckBatchProcessing": RetryableTaskState("CheckBatchProcessing", check_batch_processing, "ReceiveMessagesFromQueue"),
        "ReceiveMessagesFromQueue": TaskState("ReceiveMessagesFromQueue", receive_messages_from_queue, "EndState"),
        "EndState": TaskState("End", lambda data: (None, data))  # Estado final
    }

    # Inicializar y ejecutar la máquina de estados
    sm = StateMachine(states)
    data = {
        "processingRequired": True  # Ajusta esto para probar diferentes caminos
    }
    # Registra el inicio de la ejecución de la tarea
    logging.info("Starting state machine execution")
    final_state, final_data = sm.execute(data)
    logging.info(f"Final state: {final_state}")
    logging.info(f"Final data: {final_data}")