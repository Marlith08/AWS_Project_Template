import pandas as pd
from tests.utils.state_machine import StateMachine

class TaskState:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def execute(self, data):
        return self.task(data)

# Funciones de los estados
def load_data(data):
    print("Executing load_data")
    # Cargar datos desde un archivo Excel
    file_path = '../processed_data.xlsx'
    df = pd.read_excel(file_path)
    data["loaded_data"] = df.to_dict(orient='records')
    return "process_data1", data

def process_data1(data):
    print("Executing process_data1")
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
    print("Executing process_data2")
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
    print("Executing store_data")
    # Actualizar el archivo Excel con los datos procesados
    file_path = 'processed_data_new.xlsx'
    df = pd.DataFrame(data["processed_data"])
    df.to_excel(file_path, index=False, header=True)
    return "end", {"message": "Data stored successfully!"}

def end(data):
    print(f"StateMachine succeeded with result: {data}")
    return None, data

# Definir los estados usando TaskState
states = {
    "load_data": TaskState("load_data", load_data),
    "process_data1": TaskState("process_data1", process_data1),
    "process_data2": TaskState("process_data2", process_data2),
    "store_data": TaskState("store_data", store_data),
    "end": TaskState("end", end)
}

pos = {
    "Start": (0, 1),
    "load_data": (0, 0),
    "process_data1": (0, -1),
    "process_data2": (0, -2),
    "store_data": (0, -3),
    "end": (0, -4)
}

# Crear la máquina de estados y definir las transiciones
sm = StateMachine(states, "load_data", pos)
sm.add_transition("Start", "load_data")
sm.add_transition("load_data", "process_data1")
sm.add_transition("process_data1", "process_data2")
sm.add_transition("process_data2", "store_data")
sm.add_transition("store_data", "end")

# Ejecutar la máquina de estados
initial_data = {}
print("Executing Start")
sm.execute(initial_data)