import logging
from src.step_functions.state.task_state import TaskState
from src.step_functions.state.choice_state import ChoiceState
from src.step_functions.stateMachine import StateMachine
from src.step_functions.state.parallel_state import ParallelState
from src.amazon_s3.receive_data_from_s3 import receive_data_from_s3
from src.amazon_s3.save_advanced_results_to_s3 import save_advanced_results_to_s3
from src.amazon_s3.store_raw_data_to_s3 import store_raw_data_to_s3
from src.batch.check_batch_processing import check_batch_processing
from src.dynamoDB.save_to_dynamodb import save_to_dynamodb
from src.lambda_p.advanced_processing import advanced_processing
from src.lambda_p.process_data_with_lambda import process_data_with_lambda
from src.sns.notify_processing_complete import notify_processing_complete
from src.sns.notify_procesesing_partial import notify_procesesing_partial
from src.sqs.receive_messages_from_queue import receive_messages_from_queue

if __name__ == "__main__":
    # Configuración básica de logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Definir estados y sus tareas
    states = {
        "ReceiveDataFromS3": TaskState("ReceiveDataFromS3", receive_data_from_s3, "ParallelProcessing"),
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
        "InvokeLambdaForAdvancedProcessing": TaskState("InvokeLambdaForAdvancedProcessing", advanced_processing,
                                                       "SaveAdvancedResultsToS3"),
        "SaveAdvancedResultsToS3": TaskState("SaveAdvancedResultsToS3", save_advanced_results_to_s3,
                                             "NotifyAdvancedProcessingComplete"),
        "NotifyAdvancedProcessingComplete": TaskState("NotifyAdvancedProcessingComplete", notify_processing_complete,
                                                      "CheckBatchProcessing"),
        "CheckBatchProcessing": TaskState("CheckBatchProcessing", check_batch_processing, "ReceiveMessagesFromQueue"),
        "ReceiveMessagesFromQueue": TaskState("ReceiveMessagesFromQueue", receive_messages_from_queue,
                                              "EndState"),
        "EndState": TaskState("End", lambda data: (None, data))
    }

    # Inicializar y ejecutar la máquina de estados
    sm = StateMachine(states)
    data = {
        "processingRequired": True  #Lo podemos modificar
    }
    # Registra el inicio de la ejecución de la tarea
    logging.info("Starting state machine execution")
    final_state, final_data = sm.execute(data)
    logging.info(f"Final state: {final_state}") # Registra el inicio de la ejecución de la tarea
    logging.info(f"Final data: {final_data}")   # Registra el inicio de la ejecución de la tarea