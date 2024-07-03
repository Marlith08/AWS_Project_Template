import logging
from datetime import datetime
import time
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SimulatedStepFunctions:
    def __init__(self):
        self.state_machines = {}
        self.executions = {}
        self.current_execution_arn = None

    def create_state_machine(self, name, states):
        """
        Simula la creación de una máquina de estado.
        """
        state_machine_arn = f"arn:aws:states:local:123456789012:stateMachine:{name}"
        self.state_machines[state_machine_arn] = {
            "name": name,
            "states": states,
            "creationDate": datetime.now().isoformat()
        }
        logging.info(f"Máquina de estado '{name}' creada con éxito. ARN: {state_machine_arn}")
        return state_machine_arn

    def list_state_machines(self):
        """
        Simula listar todas las máquinas de estado.
        """
        return [{"stateMachineArn": arn, **details} for arn, details in self.state_machines.items()]

    def start_execution(self, state_machine_arn, input_data):
        """
        Simula iniciar una ejecución de la máquina de estado.
        """
        if state_machine_arn not in self.state_machines:
            logging.error(f"Máquina de estado no encontrada: {state_machine_arn}")
            return None

        execution_arn = f"{state_machine_arn}/execution/{len(self.executions) + 1}"
        self.executions[execution_arn] = {
            "stateMachineArn": state_machine_arn,
            "input": input_data,
            "status": "RUNNING",
            "startDate": datetime.now().isoformat()
        }
        logging.info(f"Ejecución iniciada con éxito. ARN: {execution_arn}")

        self.current_execution_arn = execution_arn

        # Simulación de la ejecución de la máquina de estado
        state_machine = self.state_machines[state_machine_arn]
        states = state_machine["states"]
        self._execute_state_machine(states, input_data)

        if self.executions[execution_arn]["status"] != "FAILED":
            self.executions[execution_arn]["status"] = "SUCCEEDED"
            self.executions[execution_arn]["stopDate"] = datetime.now().isoformat()

        return execution_arn

    def _execute_state_machine(self, states, input_data):
        """
        Simula la ejecución de la definición de la máquina de estado.
        """
        current_state = list(states.keys())[0]

        while current_state:
            state = states[current_state]
            logging.info(f"Executing {current_state}")

            try:
                current_state, input_data = state(input_data)
            except Exception as e:
                error_message = str(e)
                logging.error(f"Error en la ejecución: {error_message}")

                # Handle specific errors
                if "DataLimitExceeded" in error_message:
                    self.handle_error(self.current_execution_arn, "Data limit exceeded")
                    break
                elif "Timeout" in error_message:
                    self.handle_error(self.current_execution_arn, "Timeout error")
                    break
                elif "TaskFailed" in error_message:
                    self.handle_error(self.current_execution_arn, "Task failed")
                    break
                else:
                    self.handle_error(self.current_execution_arn, "Unknown error occurred")
                    break

    def get_execution_status(self, execution_arn):
        """
        Obtiene el estado actual de una ejecución de la máquina de estado.
        """
        if execution_arn in self.executions:
            return self.executions[execution_arn]["status"]
        else:
            logging.error(f"Ejecución no encontrada: {execution_arn}")
            return None

    def stop_execution(self, execution_arn):
        """
        Simula detener una ejecución de la máquina de estado.
        """
        if execution_arn in self.executions:
            self.executions[execution_arn]["status"] = "STOPPED"
            logging.info(f"Ejecución detenida con éxito: {execution_arn}")
            return True
        else:
            logging.error(f"Ejecución no encontrada: {execution_arn}")
            return False

    def handle_error(self, execution_arn, error_message):
        """
        Maneja un error en una ejecución de la máquina de estado.
        """
        if execution_arn in self.executions:
            self.executions[execution_arn]["status"] = "FAILED"
            self.executions[execution_arn]["error_message"] = error_message
            logging.error(f"Ejecución fallida: {execution_arn}. Error: {error_message}")
        else:
            logging.error(f"Ejecución no encontrada: {execution_arn}")

# Funciones para la primera máquina de estado
def state_sum(data):
    sum_values = data["num1"] + data["num2"]
    if sum_values > 50:
        raise Exception("DataLimitExceeded")
    return "state_check_sum", {"sum_values": sum_values}

def state_check_sum(data):
    sum_values = data["sum_values"]
    if sum_values < 20:
        return "state_AddFive", data
    else:
        return "state_PrintMessage", data

def state_AddFive(data):
    data["sum_values"] += 5
    return "End", data

def state_PrintMessage(data):
    sum_values = data["sum_values"]
    return "End", data

def End(data):
    return None, data

# Funciones para la segunda máquina de estado
def carga_datos(data):
    if not data.get('datos_cargados', False):
        logging.info("\nCargando datos desde la base de datos... \n")
        time.sleep(1)  # Simulación de proceso de carga
        data["datos_cargados"] = True
    return data

def limpieza_datos(data):
    if not data.get('datos_limpios', False):
        logging.info("Limpiando y preprocesando datos... \n")
        time.sleep(3)  # Simulación de proceso de limpieza
        data["datos_limpios"] = True
    return data

def analisis_datos(data):
    logging.info("Realizando análisis estadístico de los datos... \n")
    time.sleep(5)  # Simulación de proceso de análisis
    data["resultados_analisis"] = {"media": 25.4, "desviacion_std": 4.2}
    return data

# Funciones para la tercera máquina de estado
def load_data(data):
    file_path = '../processed_data.xlsx'
    df = pd.read_excel(file_path)
    data["loaded_data"] = df.to_dict(orient='records')
    return "process_data1", data

def process_data1(data):
    processed_data = []
    for item in data["loaded_data"]:
        processed_item = {
            "id": item["id"],
            "processed_value": item["processed_value"].upper()
        }
        processed_data.append(processed_item)
    data["processed_data"] = processed_data
    return "process_data2", data

def process_data2(data):
    processed_data = []
    for item in data["loaded_data"]:
        processed_value = item["processed_value"].upper()
        processed_value_without_spaces = processed_value.replace(" ", "")  # Remover espacios
        processed_item = {
            "id": item["id"],
            "processed_value": processed_value,
            "length": len(processed_value_without_spaces)  # Calcula la longitud sin espacios
        }
        processed_data.append(processed_item)
    data["processed_data"] = processed_data
    return "store_data", data

def store_data(data):
    file_path = 'processed_data_new.xlsx'
    df = pd.DataFrame(data["processed_data"])
    df.to_excel(file_path, index=False, header=True)
    return "end", {"message": "Data stored successfully!"}

def end(data):
    print(f"Final result: {data}")
    return None, data

# Definición de estados para las máquinas de estado
states_1 = {
    "state_sum": state_sum,
    "state_check_sum": state_check_sum,
    "state_AddFive": state_AddFive,
    "state_PrintMessage": state_PrintMessage,
    "End": End
}

states_2 = {
    "carga_datos": lambda data: ("limpieza_datos", carga_datos(data)),
    "limpieza_datos": lambda data: ("analisis_datos", limpieza_datos(data)),
    "analisis_datos": lambda data: ("End", analisis_datos(data)),
    "End": lambda data: (None, data)
}

states_3 = {
    "load_data": load_data,
    "process_data1": process_data1,
    "process_data2": process_data2,
    "store_data": store_data,
    "end": end
}

if __name__ == "__main__":
    client = SimulatedStepFunctions()

    # Crear y ejecutar la primera máquina de estado
    state_machine_arn_1 = client.create_state_machine("StateMachine1", states_1)
    execution_input_1 = {"num1": 23, "num2": 10}
    execution_arn_1 = client.start_execution(state_machine_arn_1, execution_input_1)

    # Crear y ejecutar la segunda máquina de estado
    state_machine_arn_2 = client.create_state_machine("StateMachine2", states_2)
    execution_input_2 = {"datos_cargados": True, "datos_limpios": True}
    execution_arn_2 = client.start_execution(state_machine_arn_2, execution_input_2)

    # Crear y ejecutar la tercera máquina de estado
    state_machine_arn_3 = client.create_state_machine("StateMachine3", states_3)
    execution_input_3 = {}
    execution_arn_3 = client.start_execution(state_machine_arn_3, execution_input_3)

    # Listar las máquinas de estado
    state_machines = client.list_state_machines()
    print("Máquinas de estado disponibles:")
    for sm in state_machines:
        print(sm)